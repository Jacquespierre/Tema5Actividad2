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

    def grupoPago():
        var.pay = []
        try:
            for i, data in enumerate(var.ui.grupoPago.buttons()):
                if data.isChecked() and i==0:
                    #print('Pago en efectivo')
                    var.pay.append('Efectivo')
                if data.isChecked() and i==1:
                    #print('Pago con tarjeta')
                    var.pay.append('Tarjeta')
                if data.isChecked() and i == 2:
                    #print('Pago con transferencia')
                    var.pay.append('Transferencia')
                #print(var.pay)
            return var.pay

        except Exception as error:
            print('Error: %s ' % str(error))