from PyQt5 import QtSql, QtWidgets

import var


class Conexion():

    def db_connect(filename):

        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(filename)
        if not db.open():
            QtWidgets.QMessageBox.critical(None, 'No se puede abrir la base de datos',
                                           'No se puede establecer conexión.\n ' 'Haz Click para Cancelar.',
                                           QtWidgets.QMessageBox.Cancel)
            return False
        else:
            print('Conexion Establecida')
        return True

    def cargarCli(clientes):
        query = QtSql.QSqlQuery()
        query.prepare(
            'insert into clientes (dni, apellidos, nombre, direccion, provincia, sexo, formapago, fechaalta, envio)'
            'VALUES (:dni, :apellidos, :nombre, :direccion, :provincia, :sexo, :formapago, :fechaalta, :envio)')
        query.bindValue(':dni', str(clientes[0]))
        query.bindValue(':apellidos', str(clientes[1]))
        query.bindValue(':nombre', str(clientes[2]))
        query.bindValue(':direccion', str(clientes[3]))
        query.bindValue(':provincia', str(clientes[4]))
        query.bindValue(':sexo', str(clientes[5]))
        # pagos
        query.bindValue(':formapago', str(clientes[6]))
        query.bindValue(':fechaalta', str(clientes[7]))
        query.bindValue(':envio', str(clientes[8]))
        # print (pagos)
        if query.exec_():
            print("Inserción correcta")
            Conexion.mostrarClientes(clientes)
        else:
            print("Error: ", query.lastError().text())

    def mostrarClientes(self):
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select dni, apellidos, nombre, direccion, '
                      'provincia, sexo, formapago, fechaalta, envio from clientes')
        if query.exec_():
            while query.next():
                dni = query.value(0)
                apellidos = query.value(1)
                nombre = query.value(2)
                direccion = query.value(3)
                provincia = query.value(4)
                sexo = query.value(5)
                formapago = query.value(6)
                fechaalta = query.value(7)
                envio = query.value(8)
                var.ui.tableWidget.setRowCount(index + 1)
                var.ui.tableWidget.setItem(index, 0, QtWidgets.QTableWidgetItem(dni))
                var.ui.tableWidget.setItem(index, 1, QtWidgets.QTableWidgetItem(apellidos))
                var.ui.tableWidget.setItem(index, 2, QtWidgets.QTableWidgetItem(nombre))
                var.ui.tableWidget.setItem(index, 3, QtWidgets.QTableWidgetItem(direccion))
                var.ui.tableWidget.setItem(index, 4, QtWidgets.QTableWidgetItem(provincia))
                var.ui.tableWidget.setItem(index, 5, QtWidgets.QTableWidgetItem(sexo))
                var.ui.tableWidget.setItem(index, 6, QtWidgets.QTableWidgetItem(formapago))
                var.ui.tableWidget.setItem(index, 7, QtWidgets.QTableWidgetItem(fechaalta))
                var.ui.tableWidget.setItem(index, 8, QtWidgets.QTableWidgetItem(envio))
                index += 1
        else:
            # Conexion.mostrarClientes(self)
            print("Error mostrar los clientes: ", query.lastError().text())

    def bajaCliente(dni):
        query = QtSql.QSqlQuery()
        query.prepare('delete from clientes where dni = :dni')
        query.bindValue(':dni', dni)

        if query.exec_():
            print('Baja de clientes')
            var.ui.label_2.setText('Cliente con dni ' + dni + ' dado de baja')
        else:
            print('Error mostrar putos clientes: ', query.lastError().text())

    def modificar(newdata):
        query = QtSql.QSqlQuery()
        dni = newdata[0]
        query.prepare(
            'update clientes set dni=:dni, apellidos=:apellidos, nombre=:nombre, direccion=:direccion, provincia=:provincia, sexo=:sexo, '
            'formapago=:formapago, fechaalta=:fechaalta, envio=:envio where dni=:dni')
        query.bindValue(':dni', str(dni))
        query.bindValue(':apellidos', str(newdata[1]))
        query.bindValue(':nombre', str(newdata[2]))
        query.bindValue(':direccion', str(newdata[3]))
        query.bindValue(':provincia', str(newdata[4]))
        query.bindValue(':sexo', str(newdata[5]))
        query.bindValue(':formapago', str(newdata[6]))
        query.bindValue(':fechaalta', str(newdata[7]))
        query.bindValue(':envio', str(newdata[8]))

        if query.exec_():
            print('Cliente modificado')
            var.ui.label_2.setText('Cliente con dni ' + str(newdata[0]) + ' modificado.')
        else:
            print("Error modificar cliente: ", query.lastError().text())

    def buscarCliente():
        codigo = var.ui.CampoDNI.text()
        query = QtSql.QSqlQuery()
        query.prepare('select dni, apellidos, nombre, direccion, provincia, '
                      'sexo, formapago, fechaalta, envio from clientes where dni=:dni')
        query.bindValue(':dni', codigo)

        if query.exec_():
            while query.next():
                dni = query.value(0)
                apellidos = query.value(1)
                nombre = query.value(2)
                direccion = query.value(3)
                provincia = query.value(4)
                sexo = query.value(5)
                formapago = query.value(6)
                fechaalta = query.value(7)
                envio = query.value(8)

                var.ui.CampoDNI.setText(dni)
                var.ui.CampoApellidos.setText(apellidos)
                var.ui.CampoNombre.setText(nombre)
                var.ui.CampoApellidos_2.setText(direccion)
                #prov = ['Álava', 'Albacete', 'Alicante', 'Almería', 'Asturias', 'Ávila', 'Badajoz', 'Barcelona',
                #        'Burgos', 'Cáceres', 'Cádiz', 'Cantabria', 'Castellón', 'Ceuta', 'Ciudad', 'Real', 'Córdoba',
                #        'Cuenca', 'Girona', 'Las Palmas', 'Granada', 'Guadalajara', 'Guipúzcoa', 'Huelva', 'Huesca',
                #        'Illes Balears', 'Jaén', 'A Coruña', 'La Rioja', 'León', 'Lleida', 'Lugo', 'Madrid', 'Málaga',
                ##        'Melilla', 'Murcia', 'Navarra', 'Ourense', 'Palencia', 'Pontevedra', 'Salamanca', 'Segovia',
                #        'Sevilla', 'Soria', 'Tarragona', 'Santa Cruz de Tenerife', 'Teruel', 'Toledo', 'Valencia',
                #        'Valladolid', 'Vizcaya', 'Zamora', 'Zaragoza']
                #var.ui.ComboBox.setCurrentIndex.range(52)
                #if (prov not in provincia):
                #    print('Provincia no está en la lista')

                if (provincia == "Álava"):
                    var.ui.comboBox.setCurrentIndex(1)
                elif (provincia == "Albacete"):
                    var.ui.comboBox.setCurrentIndex(2)
                elif (provincia == "Alicante"):
                    var.ui.comboBox.setCurrentIndex(3)
                elif (provincia == "Almería"):
                    var.ui.comboBox.setCurrentIndex(4)

                elif (provincia == "Asturias"):
                    var.ui.comboBox.setCurrentIndex(5)
                elif (provincia == "Ávila"):
                    var.ui.comboBox.setCurrentIndex(6)
                elif (provincia == "Badajoz"):
                    var.ui.comboBox.setCurrentIndex(7)
                elif (provincia == "Barcelona"):
                    var.ui.comboBox.setCurrentIndex(8)

                elif (provincia == "Burgos"):
                    var.ui.comboBox.setCurrentIndex(9)
                elif (provincia == "Cáceres"):
                    var.ui.comboBox.setCurrentIndex(10)
                elif (provincia == "Cádiz"):
                    var.ui.comboBox.setCurrentIndex(11)
                elif (provincia == "Cantabria"):
                    var.ui.comboBox.setCurrentIndex(12)

                elif (provincia == "Castellón"):
                    var.ui.comboBox.setCurrentIndex(13)
                elif (provincia == "Ciudad Real"):
                    var.ui.comboBox.setCurrentIndex(14)
                elif (provincia == "Córdoba"):
                    var.ui.comboBox.setCurrentIndex(15)
                elif (provincia == "Cuenca"):
                    var.ui.comboBox.setCurrentIndex(16)

                elif (provincia == "Gerona"):
                    var.ui.comboBox.setCurrentIndex(17)
                elif (provincia == "Granada"):
                    var.ui.comboBox.setCurrentIndex(18)
                elif (provincia == "Guadalajara"):
                    var.ui.comboBox.setCurrentIndex(19)
                elif (provincia == "Guipúzcoa"):
                    var.ui.comboBox.setCurrentIndex(20)

                elif (provincia == "Huelva"):
                    var.ui.comboBox.setCurrentIndex(21)
                elif (provincia == "Huesca"):
                    var.ui.comboBox.setCurrentIndex(22)
                elif (provincia == "Islas Baleares"):
                    var.ui.comboBox.setCurrentIndex(23)
                elif (provincia == "Jaén"):
                    var.ui.comboBox.setCurrentIndex(24)
                elif (provincia == "La Coruña"):
                    var.ui.comboBox.setCurrentIndex(25)
                elif (provincia == "La Rioja"):
                    var.ui.comboBox.setCurrentIndex(26)
                elif (provincia == "Las Palmas"):
                    var.ui.comboBox.setCurrentIndex(27)
                elif (provincia == "León"):
                    var.ui.comboBox.setCurrentIndex(28)

                elif (provincia == "Lérida"):
                    var.ui.comboBox.setCurrentIndex(29)
                elif (provincia == "Lugo"):
                    var.ui.comboBox.setCurrentIndex(30)
                elif (provincia == "Madrid"):
                    var.ui.comboBox.setCurrentIndex(31)
                elif (provincia == "Málaga"):
                    var.ui.comboBox.setCurrentIndex(32)

                elif (provincia == "Murcia"):
                    var.ui.comboBox.setCurrentIndex(33)
                elif (provincia == "Navarra"):
                    var.ui.comboBox.setCurrentIndex(34)
                elif (provincia == "Orense"):
                    var.ui.comboBox.setCurrentIndex(35)
                elif (provincia == "Palencia"):
                    var.ui.comboBox.setCurrentIndex(36)

                elif (provincia == "Pontevedra"):
                    var.ui.comboBox.setCurrentIndex(37)
                elif (provincia == "Salamanca"):
                    var.ui.comboBox.setCurrentIndex(38)
                elif (provincia == "Santa Cruz de Tenerife"):
                    var.ui.comboBox.setCurrentIndex(39)
                elif (provincia == "Segovia"):
                    var.ui.comboBox.setCurrentIndex(40)

                elif (provincia == "Sevilla"):
                    var.ui.comboBox.setCurrentIndex(41)
                elif (provincia == "Soria"):
                    var.ui.comboBox.setCurrentIndex(42)
                elif (provincia == "Tarragona"):
                    var.ui.comboBox.setCurrentIndex(43)
                elif (provincia == "Teruel"):
                    var.ui.comboBox.setCurrentIndex(44)

                elif (provincia == "Toledo"):
                    var.ui.comboBox.setCurrentIndex(45)
                elif (provincia == "Valencia"):
                    var.ui.comboBox.setCurrentIndex(46)
                elif (provincia == "Valladolid"):
                    var.ui.comboBox.setCurrentIndex(47)
                elif (provincia == "Vizcaya"):
                    var.ui.comboBox.setCurrentIndex(48)
                elif (provincia == "Zamora"):
                    var.ui.comboBox.setCurrentIndex(49)
                elif (provincia == "Zaragoza"):
                    var.ui.comboBox.setCurrentIndex(50)

                if (sexo == 'Femenino'):
                    var.ui.radioButtonFem_2.click()
                else:
                    var.ui.radioButtonFem_2.click()
                # var.ui.horizontalLayout_2(sexo)

                if (formapago == 'Efectivo'):
                    var.ui.checkEfect_2.click()
                elif (formapago == 'Tarjeta'):
                    var.ui.checkTarjeta_2.click()
                elif (formapago == 'Transferencia'):
                    var.ui.checkTransfe_2.click()

                # var.ui.metodoPago_2(formapago)
                var.ui.CampoFecha.setText(fechaalta)

                var.ui.label_3.setText(envio)

                print('Cliente con DNI' + codigo + ' se ha encontrado.')
                var.ui.label_2.setText('El cliente con DNI ' + codigo + ' se ha encontrado')
        else:
            print('Error al buscar cliente', query.lastError().text())

    def recuperarBackup(self):
        try:
            option = QtWidgets.QFileDialog.Options()
            filename = var.actionAbrir.getOpenFileName(None, 'Restaurar copia', '', '*.zip', options=option)
            clientes = str(filename[0])
            if var.actionAbrir.Accepted and filename != '' and clientes.endswith('.zip'):
                carpeta = clientes.add('s')
                shutil.unpack_archive(clientes, carpeta, 'zip')
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