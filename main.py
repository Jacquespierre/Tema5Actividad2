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
        # var.sex = (var.ui.radioButtonFem_2, var.ui.radioButtonMas_2)
        # for i in var.sex:
        #    i.toggled.connect(clients.Clientes.selSexo)
        '''
        Eventos cada de texto
        '''
        var.ui.CampoDNI.editingFinished.connect(clients.Clientes.validarDNI)
        var.ui.Aceptar.clicked.connect(clients.Clientes.validarDNI)
        var.ui.grupoSexo.buttonClicked.connect(clients.Clientes.selSexo)

        var.ui.Aceptar.clicked.connect(clients.Clientes.showClients)

        var.checkPago = (var.ui.checkEfect_2, var.ui.checkTransfe_2, var.ui.checkTarjeta_2)
        for i in var.checkPago:
            i.stateChanged.connect(events.Eventos.grupoPago)

        clients.Clientes.cargarProv()
        var.ui.comboBox.activated[str].connect(clients.Clientes.selProv)

        # var.ui.comboBox.editingFinished.connect(clients.Clientes.selProv)

        var.ui.Calendario.clicked.connect(clients.Clientes.abrirCalendar)
        #########################################################################################

        conexion.Conexion.db_connect(var.filedb)
        conexion.Conexion.mostrarClientes(self)

        var.ui.bajaClie.clicked.connect(conexion.Conexion.bajaCliente)
        var.ui.limpiar.clicked.connect(clients.Clientes.limpiarCli)
        var.ui.buscar.clicked.connect(conexion.Conexion.buscarCliente)
        var.ui.modificar.clicked.connect(clients.Clientes.showClients)
        var.ui.actualizar.clicked.connect(clients.Clientes.modificar)


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
        # diaactual = datetime.now().day
        # mesactual = datetime.now().month
        # anoactual = datetime.now().year
        # var.dlgcalendar.calendarWidget.setSelectedDate((QtCore.QDate(anoactual, mesactual, diaactual)))
        var.dlgcalendar.calendarWidget.clicked.connect(clients.Clientes.cargarFecha)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    var.avisoSalir = avisoSalir()
    var.dlgcalendar = DialogCalendar()
    window.show()
    sys.exit(app.exec())
