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

    def selSexo(self):
        try:
            if var.ui.radioButtonFem_2.isChecked():
                var.sex = 'Mujer'
                print('Marcado femenino')
            if var.ui.radioButtonMas_2.isChecked():
                var.sex = 'Hombre'
                print('Marcado masculino')
        except Exception as error:
            print('Error en módulo seccionar sexo:', error)

    def cargarProv():
        try:
            prov = [' ', 'Álava', 'Albacete', 'Alicante', 'Almería', 'Asturias', 'Ávila', 'Badajoz', 'Barcelona',
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
        try:  # Preparamos el registro
            newcli = []
            var.pay = []
            client = [var.ui.CampoDNI, var.ui.CampoApellidos, var.ui.CampoNombre, var.ui.CampoApellidos_2,
                      var.ui.comboBox, var.ui.horizontalLayout_2,var.ui.metodosPago_2, var.ui.CampoFecha]
            for i in client:
                newcli.append(i.text())
            newcli.append(var.vpro)
            # Elimina duplicados
            var.pay = set(var.pay)
            for j in var.pay:
                newcli.append(j)
            newcli.append(var.sex)
            print(newcli)
        except Exception as error:
            print('Error: %s ' % str(error))
