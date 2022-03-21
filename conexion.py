import PyQt5
from PyQt5 import QtSql, QtWidgets

import var


class Conexion():

    def db_connect(clientes):

        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(clientes)
        if not db.open():
            QtWidgets.QMessageBox.critical(None, 'No se puede abrir la base de datos',
                                           'No se puede establecer conexión.\n ' 'Haz Click para Cancelar.',
                                           QtWidgets.QMessageBox.Cancel)
            return False
        else:
            print('Conexion Establecida')
        return True

    def cargarCli(clientes):
        print("hola")
        query = QtSql.QSqlQuery()
        query.prepare('insert into clientes (dni, apellidos, nombre, direccion, provincia, sexo, formapago, fechaalta)'
                      'VALUES (:dni, :apellidos, :nombre, :direccion, :provincia, :sexo, :formapago, :fechaalta')
        query.bindValue(':dni', str(clientes[0]))
        query.bindValue(':apellidos', str(clientes[1]))
        query.bindValue(':nombre', str(clientes[2]))
        query.bindValue(':direccion', str(clientes[3]))
        query.bindValue(':provincia', str(clientes[4]))
        query.bindValue(':sexo', str(clientes[5]))
        # pagos
        query.bindValue(':formapago', str(clientes[6]))
        query.bindValue(':fechaalta', str(clientes[7]))
        # print (pagos)
        if query.exec_():
            print("Inserción correcta")
            Conexion.mostrarClientes()
        else:
            print("Error: ", query.lastError().text())

    def mostrarClientes(self):
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select dni, apellidos, nombre, direccion, provincia, sexo, formapago, fechaalta from clientes')
        if query.exec():
            while query.next():
                dni = query.value(0)
                apellidos = query.value(1)
                nombre = query.value(2)
                direccion = query.value(3)
                provincia = query.value(4)
                sexo = query.value(5)
                formapago = query.value(6)
                fechaalta = query.value(7)
                var.ui.tableWidget.setRowCount(index + 1)
                var.ui.tableWidget.setItem(index, 0, QtWidgets.QTableWidgetItem(dni))
                var.ui.tableWidget.setItem(index, 1, QtWidgets.QTableWidgetItem(apellidos))
                var.ui.tableWidget.setItem(index, 2, QtWidgets.QTableWidgetItem(nombre))
                var.ui.tableWidget.setItem(index, 3, QtWidgets.QTableWidgetItem(direccion))
                var.ui.tableWidget.setItem(index, 4, QtWidgets.QTableWidgetItem(provincia))
                var.ui.tableWidget.setItem(index, 5, QtWidgets.QTableWidgetItem(sexo))
                var.ui.tableWidget.setItem(index, 6, QtWidgets.QTableWidgetItem(formapago))
                var.ui.tableWidget.setItem(index, 7, QtWidgets.QTableWidgetItem(fechaalta))
                index += 1
        else:
            Conexion.mostrarClientes(self)
            print("Error mostrar clientes: ", query.lastError().text())



