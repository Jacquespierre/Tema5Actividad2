from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets

import os.path
import shutil
import zipfile
import xlrd
import easygui
import pandas as pd

import conexion
import clients

import sys
import var

class CopiaSeguridad():

    def Backup():
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y.%m.%d.%H.%M.%S')
            var.copia = (str(fecha)+'backup.zip')
            option = QtWidgets.QFileDialog.Options()
            directorio, filename = var.filedlgabrir.getSaveFileName(None, 'Guardar Copia', var.copia, '.zip', options=option)
            if var.filedlgabrir.Accepted and filename != '':
                fichZip = zipfile.ZipFile(var.copia, 'w')
                fichZip.write(var.filedb, os.path.basename(var.filedb), zipfile.ZIP_DEFLATED)
                fichZip.close()
                var.ui.lblstatus.setText('Base de datos copiada en un archivo ZIP')
                shutil.move(str(var.copia),str(directorio))
        except Exception as error:
            print('Error al comprimir: %s' % str(error))

    def recuperarBackup(self):
        try:
            option = QtWidgets.QFileDialog.Options()
            filename = var.filedlgabrir.getOpenFileName(None, 'Restaurar copia', '', '*.zip', options=option)
            baseDatos = str(filename[0])
            if var.filedlgabrir.Accepted and filename != '' and baseDatos.endswith('.zip'):
                carpeta = baseDatos.__add__('s')
                shutil.unpack_archive(baseDatos, carpeta, 'zip')
                directorio = os.path.basename(carpeta)
                archivo = os.listdir(directorio)
                var.filedb = archivo[0]
                conexion.Conexion.db_connect(var.filedb)
                var.ui.lblstatus.setText('Base de datos %s recuperada' % baseDatos)
                conexion.Conexion.mostrarCli(self)
            else:
                conexion.Conexion.mostrarCli(self)
                var.ui.lblstatus.setText('Para recuperar el BACKUP debe ser un archivo ZIP')
                print('El BACKUP debe ser un archivo ZIP')
        except Exception as error:
            print('Error recuperar zip base de datos: %s' % str(error))

    def importarDatos():
        file_name = easygui.fileopenbox()
        conexion.Conexion.importarExcel(file_name, pd)
