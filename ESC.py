# Script para la calibracion de los motores.

import os
import time
os.system ("sudo pigpiod") # Lanzamos la libreria de GPIO
time.sleep(1)
import pigpio # Se importa la libreria GPIO

#---------------------CONFIGURACION-------------------
ESC=4  # El PIN al que está conectado el ESC

pi = pigpio.pi()
pi.set_servo_pulsewidth(ESC, 0) # Para mandarle el pulso

max_value = 2000 # Valor maximo para el ESC
min_value = 1000  # Valor minimo para el ESC

#---------------------MANUAL------------------------
def manual_drive():
    print("Dame un valor entre el 0 y el valor maximo")
    while True:
        inp = input()
        if inp == "stop":
            stop()
            break
        elif inp == "control":
            control()
            break
        elif inp == "arm":
            arm()
            break
        else:
            pi.set_servo_pulsewidth(ESC,inp)

#---------------------CALIBRAR------------------------
def calibrate():
    pi.set_servo_pulsewidth(ESC, 0)
    print("Desconecta la bateria y dale al ENTER")
    inp = input()
    if inp == '': # El ENTER
        pi.set_servo_pulsewidth(ESC, max_value) # Le pasamos el valor maximo
        print("Conectala, deberias escuchar dos BEPS, espera para un sonido gradual y luego dale enter")
        inp = input()
        if inp == '':
            pi.set_servo_pulsewidth(ESC, min_value) # Le enviamos el valor minimo
            print("Tono especial")
            time.sleep(3)
            pi.set_servo_pulsewidth(ESC, 0)
            time.sleep(2)
            print("Arming ESC now...")
            pi.set_servo_pulsewidth(ESC, min_value)
            time.sleep(1)
            print("Ya puedes")
            control() # De aqui puedes cambiar a la funcion que quieras

#---------------------CONTROL------------------------
def control():
    print("Si el ESC no esta calibrado y armado pulsa 'x'")
    time.sleep(1)
    speed = 1500 # Le mandamos una velocidad media
    print("Controles: ")
    print("'A' para bajar la velocidad")
    print("'D' para incrementar la velocidad")
    print("'Q' para bajar mucho la velocidad")
    print("'E' para subir mucho la velocidad")
    while True:
        pi.set_servo_pulsewidth(ESC, speed) # Le enviamos la velocidad
        inp = input()

        if inp == "q":
            speed -= 100   # Bajamos mucho la velocidad
            print ("speed = %d" % speed)
        elif inp == "e":
            speed += 100    # Subimos mucho la velocidad
            print ("speed = %d" % speed)
        elif inp == "d":
            speed += 10     # Subimos la velocidad
            print ("speed = %d" % speed)
        elif inp == "a":
            speed -= 10     # Bajamos la velocidad
            print ("speed = %d" % speed)
        elif inp == "stop":
            stop()          #going for the stop function
            break
        elif inp == "manual":
            manual_drive()
            break
        elif inp == "arm":
            arm()
            break
        else:
            print ("Que haces?")
#---------------------ARMAR------------------------
def arm():
    print ("Conecta la bateria y dale al ENTER")
    inp = input()
    if inp == '':
        pi.set_servo_pulsewidth(ESC, 0) # Enviamos 0
        time.sleep(1)
        pi.set_servo_pulsewidth(ESC, max_value) # Enviamos el maximo
        time.sleep(1)
        pi.set_servo_pulsewidth(ESC, min_value) # Enviamo el minimo
        time.sleep(1)
        control() # Vamos a la funcion de control

def stop(): # Esta funcion para el ESC
    pi.set_servo_pulsewidth(ESC, 0) # Lo apagamos
    pi.stop() # Lo paramos

#---------------------MENU------------------------
def menu(inp):
    inp = input()
    if inp == "manual":
        manual_drive()
    elif inp == "calibrate":
        calibrate()
    elif inp == "arm":
        arm()
    elif inp == "control":
        control()
    elif inp == "stop":
        stop()
    else :
        print("Prueba otra vez")
        menu(inp = input(": "))


if __name__ == "__main__": # Comienzo del programa
    print("Si es la primera vez, selecciona calibrar")
    print("calibrar OR manual OR control OR arm OR para")
    inp = input(": ")
    menu(inp)
