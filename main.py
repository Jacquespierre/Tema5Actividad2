import sys

import conexion
import var
import events
import clients
from ventana import *
from ventanaCalendario import *
from windowAviso import *
#########################################################################################

from PyQt5 import QtWidgets, QtSql

#########################################################################################


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
        var.ui.Salir.clicked.connect(events.Eventos.Salir)
        var.sex=(var.ui.radioButtonFem_2, var.ui.radioButtonMas_2)
        for i in var.sex:
            i.toggled.connect(clients.Clientes.selSexo)
        '''
        Eventos cada de texto
        '''
        var.ui.CampoDNI.editingFinished.connect(clients.Clientes.validarDNI)
        var.ui.Aceptar.clicked.connect(clients.Clientes.validarDNI)
        #var.ui.grupoSexo.buttonClicked.connect(clients.Clientes.selSexo)

        #var.ui.Aceptar.clicked.connect(clients.Clientes.showClients)
        var.ui.Aceptar.clicked.connect(DialogTable.showClients)


        var.checkPago = (var.ui.checkEfect_2, var.ui.checkTransfe_2, var.ui.checkTarjeta_2)
        for i in var.checkPago:
            i.stateChanged.connect(events.Eventos.grupoPago)

        clients.Clientes.cargarProv()
        var.ui.comboBox.activated[str].connect(clients.Clientes.selProv)

        #var.ui.comboBox.editingFinished.connect(clients.Clientes.selProv)


        var.ui.Calendario.clicked.connect(clients.Clientes.abrirCalendar)
#########################################################################################

        conexion.Conexion.db_connect(var.filedb)

        conexion.Conexion.mostrarClientes(self)

#################################################################################################

class DialogTable(QtWidgets.QTableWidget):
    def showClients(self):
        try:
            #Prepara el registro
            newcli =[]
            clitab = []
            client = [var.ui.CampoDNI, var.ui.CampoApellidos, var.ui.CampoNombre, var.ui.CampoApellidos_2,
                        var.ui.CampoFecha]
            k=0
            for i in client:
                newcli.append(i.text())
                if k < 3:
                    clitab.append(i.text())
                    k += 1

            newcli.append(var.vpro)
            #Elimina duplicados
            var.pay = set(var.pay)
#########################################################################################

            var.pay2 = clients.selPago()
            newcli.append(var.sex)
            newcli.append(var.pay2)

            if client:
                #Comprobamos que no esté valip lo principal como tableWidget
                row = 0
                column = 0
                var.ui.tableWidget.insertRow(row)
                for registro in clitab:
                    cell = QtWidgets.QTableWidgetItem(registro)
                    var.ui.tableWidget.setItem(row,column,cell)
                    column +=1

                conexion.Conexion.cargarCli(newcli)

            else:
                print("Faltan Datos")

            clients.limpiarCli(client, var.selSexo, var.checkPago)
        except Exception as error:
            print("Error cargar fecha: %s" % str(error))



#########################################################################################

            for j in var.pay:
                newcli.append(j)
            newcli.append(var.sex)
            print(newcli)
            print(clitab)
            row = 0 #disposicion de la fila, problema: coloca el último como primero en cada click
            column = 0 #disposicion de la columna
            var.ui.tableWidget.insertRow(row) #Inserta una fila nueva con cada click de botón
            for registro in clitab:
                #la celda tiene una posición fila, columa y cargamos en ella el dato
                cell=QtWidgets.QTableWidgetItem(registro) # carga en cell cada dato de la lista
                var.ui.tableWidget.setItem(row, column, cell) # lo escribe
                column +=1
        except Exception as error:
            print('Error: %s' % str(error))




class avisoSalir(QtWidgets.QDialog):
    def __init__(self):
        super(avisoSalir, self).__init__()
        var.avisoSalir = Ui_Form()
        var.avisoSalir.setupUi(self)

class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar, self).__init__()
        var.dlgcalendar = Ui_Dialog()
        var.dlgcalendar.setupUi(self)
        #diaactual = datetime.now().day
        #mesactual = datetime.now().month
        #anoactual = datetime.now().year
        #var.dlgcalendar.calendarWidget.setSelectedDate((QtCore.QDate(anoactual, mesactual, diaactual)))
        var.dlgcalendar.calendarWidget.clicked.connect(clients.Clientes.cargarFecha)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    var.avisoSalir = avisoSalir()
    var.dlgcalendar = DialogCalendar()
    window.show()
    sys.exit(app.exec())

