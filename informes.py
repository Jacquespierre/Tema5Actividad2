import os
from datetime import datetime

from PyQt5 import QtSql
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

import var


class Informes():
    def reportCli():
        try:
            var.rep = canvas.Canvas('informes/listadoClientes.pdf', pagesize=A4)
            Informes.cabecera()
            var.rep.setFont('Helvetica-Bold', size=8)
            textListado: str ='Listado de Clientes'
            var.rep.drawString(255, 735, textListado)
            var.rep.line(45, 730, 525, 730)
            itemCli = ['DNI', 'APELLIDOS', 'NOMBRE', 'FECHA ALTA']
            var.rep.drawString(50, 710, itemCli[0])
            var.rep.drawString(180, 710, itemCli[1])
            var.rep.drawString(280, 710, itemCli[2])
            var.rep.drawString(400, 710, itemCli[3])
            var.rep.line(45, 703, 525, 703)
            query = QtSql.QSqlQuery()
            query.prepare('select dni, apellidos, nombre, fechaalta  '
                          'from clientes order by apellidos, nombre')
            var.rep.setFont('Helvetica', size=8)
            if query.exec_():
                i = 50
                j = 690
                while query.next():
                    var.rep.drawString(i, j, str(query.value(0)))
                    var.rep.drawString(i + 100, j, str(query.value(1)))
                    var.rep.drawString(i + 250, j, str(query.value(2)))
                    var.rep.drawString(i + 350, j, str(query.value(3)))
                    j = j - 30
            Informes.pie(textListado)
            var.rep.save()
            rootPath = ".\\informes"
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('.pdf'):
                    os.startfile("%s/%s" % (rootPath, file))
                cont += 1
        except Exception as error:
            print('Error reporcli %s' % str(error))

    def cabecera():
        try:
            logo = 'imagenes\logo.png'
            var.rep.setTitle('INFORME RANDOM')
            var.rep.setAuthor('Santiago Freitas')
            var.rep.setFont('Helvetica', size=10)
            var.rep.line(45, 820, 525, 820)
            var.rep.line(45, 745, 525, 745)
            textcif = '123456789Z'
            textnom = 'Base de Datos RANDOM CLUB'
            textdir = 'Calle falsa, 123'
            texttlfo = '987654321'
            var.rep.drawString(50, 805, textcif)
            var.rep.drawString(50, 790, textnom)
            var.rep.drawString(50, 775, textdir)
            var.rep.drawString(50, 760, texttlfo)
            var.rep.drawImage(logo, 450, 752, 70, 60)
        except Exception as error:
            print('Error en la cabecera del informe %s' % str(error))

    def pie(textListado):
        try:
            var.rep.line(50, 50, 525, 50)
            fecha = datetime.today()
            fecha = fecha.strftime('%d.%m.%Y %H.%M.%S')
            var.rep.setFont('Helvetica-Oblique', size=7)
            var.rep.drawString(460, 40, str(fecha))
            var.rep.drawString(275, 40, str('Página %s' % var.rep.getPageNumber()))
            var.rep.drawImage(50, 40, str(textListado))
        except Exception as error:
            print('Error en el pie del informe %s' % str(error))
