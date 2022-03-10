import sys
import var

class Eventos:

    def Salir(self):
        try:
            var.avisoSalir.show()
            if var.avisoSalir.exec():
                sys.exit()
            else:
                var.avisoSalir.hide()
        except Exception as error:
            print("Error %s:" % str(error))

    def grupoPago(self):
        var.pay = []
        try:
            #for i, data in enumerate(var.ui.metodosPago_2.buttons()):
            if var.ui.checkEfect_2.isChecked():
                print('Pago en efectivo')
                    #var.pay.append('Efectivo')
            if var.ui.checkTarjeta_2.isChecked():
                print('Pago con tarjeta')
                    #var.pay.append('Tarjeta')
            if var.ui.checkTransfe_2.isChecked():
                print('Pago con transferencia')
                    #var.pay.append('Transferencia')
            #print(var.pay)
            #return var.pay

        except Exception as error:
            print('Error: %s ' % str(error))

