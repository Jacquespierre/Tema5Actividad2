import sys
import var
import sqlite3

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

    def formaEnvio():
        try:
            envio = var.ui.spinEnvio.value()
            listaEnvio = ['Recogida por cliente',
                                'Envío nacional paquetería exprés urgente',
                                'Envío nacional paquetería normal',
                                'Envío internacional']
            var.formaEnvio = listaEnvio[envio]
            var.ui.label_3.setText(var.formaEnvio)
        except Exception as error:
            print('Error al seleccionar envio: %' % str(error))

    def Abrir(self):
        try:
            var.actionAbrir.show()
        except Exception as error:
            print('Error al abrir el explorador: %s' % str(error))

    def conexionBaseDatos(clientes):
        try:
            conexion = sqlite3.connect(clientes)

            return conexion

        except Exception as error:
            print('Se produujo un error al crear la conexion: %s' % str(error))

    def restaurarCopia(conexion,clientes):
        with open(clientes,'r') as f:
            sql=f.read()

            try:
                cursor = conexion.cursor()
                cursor.executescript(sql)

                cursor.close()
            except sqlite3.Error as e:
                print('Se ha producido un error al restaurar la base de datos: ', e)

    conexion = nuevaConexion('CopiaBaseDatos/clientes.db')

    if conexion:
       conexion.close()