from PyQt5 import QtWidgets

import conexion
import events
import var


class Clientes():
    def validarDNI():
        try:
            dni = var.ui.CampoDNI.text()
            var.ui.CampoDNI.setText(dni.upper())
            tabla = 'TRWAGMYFPDXBNJZSQVHLCKE'  # letras dni
            dig_ext = 'XYZ'  # digito
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = '1234567890'
            dni = dni.upper()  # conver la letra mayusculas
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    var.ui.label.setStyleSheet('QLabel {color: green;}')
                    var.ui.label.setText('V')
                else:
                    var.ui.label.setStyleSheet('QLabel {color: red;}')
                    var.ui.label.setText('X')
            else:
                var.ui.label.setStyleSheet('QLabel {color: red;}')
                var.ui.label.setText('X')
        except Exception as error:
            print('Error en modulo validar DNI', error)

    def pay(self):
        try:
            var.pay = []
            for i, data in enumerate(var.ui.grupoPago.buttons()):
                if data.isChecked() and i == 0:
                    var.pay = 'Efectivo'
                    print('Pago con efectivo')
                if data.isChecked() and i == 1:
                    var.pay = 'Tarjeta'
                    print('Pago con tarjeta')
                if data.isChecked() and i == 2:
                    var.pay = 'Transferencia'
                    print('Pago con transferencia')
            return var.pay

        except Exception as error:
            print('Error selPago, ' % str(error))

    def selSexo(self):
        try:
            if var.ui.radioButtonFem_2.isChecked():
                var.sex = 'Mujer'
                print('Marcado femenino')
            if var.ui.radioButtonMas_2.isChecked():
                var.sex = 'Hombre'
                print('Marcado masculino')
        except Exception as error:
            print('Error en módlo seccionar sexo:', error)

    def cargarProv():
        try:
            prov = ['Selecciona provincia', 'Álava', 'Albacete', 'Alicante', 'Almería', 'Asturias', 'Ávila', 'Badajoz', 'Barcelona',
                    'Burgos', 'Cáceres', 'Cádiz', 'Cantabria', 'Castellón', 'Ceuta', 'Ciudad', 'Real', 'Córdoba',
                    'Cuenca', 'Girona', 'Las Palmas', 'Granada', 'Guadalajara', 'Guipúzcoa', 'Huelva', 'Huesca',
                    'Illes Balears', 'Jaén', 'A Coruña', 'La Rioja', 'León', 'Lleida', 'Lugo', 'Madrid', 'Málaga',
                    'Melilla', 'Murcia', 'Navarra', 'Ourense', 'Palencia', 'Pontevedra', 'Salamanca', 'Segovia',
                    'Sevilla', 'Soria', 'Tarragona', 'Santa Cruz de Tenerife', 'Teruel', 'Toledo', 'Valencia',
                    'Valladolid', 'Vizcaya', 'Zamora', 'Zaragoza']
            for i in prov:
                var.ui.comboBox.addItem(i)
        except  Exception as error:
            print('Error: %s' % str(error))

    def selProv(prov):
        try:
            print('Has seleccionado la provincia de ', prov)
            # return prov
            var.vpro = prov
        except Exception as error:
            print('Error: %s ' % str(error))

    def abrirCalendar(self):
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print('Error: %s' % str(error))

    def cargarFecha(qDate):
        try:
            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.CampoFecha.setText(str(data))
            var.dlgcalendar.hide()
        except Exception as error:
            print('Error al cargar fecha: %s' % str(error))

    def showClients(self):
        try:
            # Prepara el registro
            newcli = []
            clitab = []
            client = [var.ui.CampoDNI, var.ui.CampoApellidos, var.ui.CampoNombre, var.ui.CampoApellidos_2]
            k = 0
            for i in client:
                newcli.append(i.text())
                if k < 9:
                    clitab.append(i.text())
                    k += 1

            # Elimina duplicados
            var.pay = set(var.pay)
            #########################################################################################

            var.pay2 = events.Eventos.grupoPago()
            newcli.append(var.vpro)
            newcli.append(var.sex)
            newcli.append(var.pay[0])
            newcli.append(var.ui.CampoFecha.text())

            #########################################################################################
            newcli.append(var.formaEnvio)
            #########################################################################################

            if client:
                # Comprobamos que no esté vacio lo principal como tableWidget
                row = 0
                column = 0
                var.ui.tableWidget.insertRow(row)
                for registro in clitab:
                    cell = QtWidgets.QTableWidgetItem(registro)
                    var.ui.tableWidget.setItem(row, column, cell)
                    column += 1

                conexion.Conexion.cargarCli(newcli)

            else:
                print("Faltan Datos")
            print(newcli)
            # clients.limpiarCli(client, var.selSexo, var.checkPago)
        except Exception as error:
            print("Error alta cliente: %s" % str(error))

    def bajaClie(self):
        try:
            dni = var.ui.CampoDNI.text()
            conexion.Conexion.bajaCliente(dni)
            conexion.Conexion.mostrarClientes(self)
            # Clientes.limpiarCli()

        except Exception as error:
            print('Error cargar clientes: %s ' % str(error))

    def modificar(self):
        try:
            newdata = []
            client = [var.ui.CampoDNI, var.ui.CampoApellidos, var.ui.CampoNombre, var.ui.CampoApellidos_2]
            for i in client:
                newdata.append(i.text())
            newdata.append(var.ui.comboBox.currentText())
            newdata.append(var.sex)
            var.pay = events.Eventos.grupoPago()
            print(var.pay)
            newdata.append(var.pay)
            newdata.append(var.ui.CampoFecha.text())
            newdata.append(var.listaEnvio)
            print(newdata)
            conexion.Conexion.modificar(newdata)
            conexion.Conexion.mostrarClientes(self)

        except Exception as error:
            print('Error al cargar clientes: %s' % str(error))

    def limpiarCli(self):
        var.ui.CampoDNI.setText("")
        var.ui.CampoFecha.setText("")
        var.ui.CampoApellidos.setText("")
        var.ui.CampoNombre.setText("")
        var.ui.CampoApellidos_2.setText("")
        var.ui.comboBox.setCurrentIndex(0)
        var.ui.spinEdad.setValue(0)
        var.ui.label_3.setText("")

        var.ui.grupoSexo.setExclusive(False)
        var.ui.radioButtonFem_2.setChecked(False)
        var.ui.radioButtonMas_2.setChecked(False)
        var.ui.grupoSexo.setExclusive(True)

        var.ui.grupoPago.setExclusive(False)
        var.ui.checkEfect_2.setChecked(False)
        var.ui.checkTarjeta_2.setChecked(False)
        var.ui.checkTransfe_2.setChecked(False)
        var.ui.grupoPago.setExclusive(True)
