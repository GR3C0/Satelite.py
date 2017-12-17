# Satelite made in spain by Diego Morell con el objetivo de recoger datos
# suborbitales y superarme a mi mismo y sobre todo demostrar que lo he conseguido
#
# Empiezo este satelite el dia 17/12/2017 a las 23:29

# Utilizaré python 3, el módulo de sense hat para controlar el hardware y
# el módulo de astropy para estudiar los datos recogidos por los sensores
# Página de pruebas: https://trinket.io/sense-hat


#--------------------------------------
#----Archivo principal del satelite----
#--------------------------------------

__author__ = "Diego Morell"
__email__ = "diegomorellmasip@gmail.com"

import astropy as sp
from sense_hat import SenseHat
import time

sense = SenseHat()


# Nota: guiño final, hacer que pongas cosas en los leds

#---------Prueba de sensores-------

def temperatura():
    while True:
        temp = sense.get_temperature() # Obtener la temperatura
        print(temp, "grados")


def presion():
    while True:
        pres = sense.get_pressure() # Obtener la presion
        print(pres, "bares")

def humedad():
    while True:
        hum = sense.get_humidity() # Obtener la humedad
        print(hum)

# El sense hat tiene un IMU que son un acelerometro, un giroscopio y un magnetometro

def orientacion():
    while True:
        o = sense.get_orientation()
        # Hay tres formas de movimiento: Pitch, Yaw, y Roll
        pitch = o["pitch"]
        roll = o["roll"]
        yaw = o["yaw"]
        print("pitch {0} roll {1} yaw {2}".format(pitch,roll, yaw))


def menu(respuesta):
    if respuesta == "1": # Si ha elegido la temperatura
        temperatura()

    elif respuesta == "2": # Si ha elegido la presion
        presion()

    elif respuesta == "3": # Si ha elegido la humedad
        orientacion()

    else: # En caso de que se quivoque
        print("No se que dices")
        menu(respuesta = input("Que quieres hacer?"))


# Aquí se empieza a ejecutar todo
if __name__ == "__main__":
    acciones = ['temperatura = 1', 'presion = 2', 'humedad = 3']
    print(acciones)
    respuesta = input("Que quieres hacer?")
    menu(respuesta)
