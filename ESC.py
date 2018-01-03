# Script para la calibracion de los motores.

import os
import time
os.system ("sudo pigpiod") # Lanzamos la libreria de GPIO
time.sleep(1)
import pigpio # Se importa la libreria GPIO

ESC=4  # El PIN al que está conectado el ESC

pi = pigpio.pi()
pulso = pi.set_servo_pulsewidth()
pulso(ESC,0)

max_value = 2000 # Valor maximo para el ESC
min_value = 1000  # Valor minimo para el ESC
print "Si es la primera vez, selecciona calibrar"
print "calibrar OR manual OR control OR arm OR para"

def manual_drive():
    print "Dame un valor entre el 0 y el valor maximo"
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
            pulso(ESC,inp)

def calibrate():
    pulso(ESC, 0)
    print("Desconecta la bateria y dale al ENTER")
    inp = input()
    if inp == '': # El ENTER
        pulso(ESC, max_value) # Le pasamos el valor maximo
        print("Conectala, deberias escuchar dos BEPS, espera para un sonido gradual y luego dale enter")
        inp = input()
        if inp == '':
            pulso(ESC, min_value) # Le enviamos el valor minimo
            print("Tono especial")
            time.sleep(3)
            pulso(ESC, 0)
            time.sleep(2)
            print("Arming ESC now...")
            pulso(ESC, min_value)
            time.sleep(1)
            print("Ya puedes")
            control() # De aqui puedes cambiar a la funcion que quieras

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
        pulso(ESC, speed) # Le enviamos la velocidad
        inp = input()

        if inp == "q":
            speed -= 100    # decrementing the speed like hell
            print "speed = %d" % speed
        elif inp == "e":
            speed += 100    # incrementing the speed like hell
            print "speed = %d" % speed
        elif inp == "d":
            speed += 10     # incrementing the speed
            print "speed = %d" % speed
        elif inp == "a":
            speed -= 10     # decrementing the speed
            print "speed = %d" % speed
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
            print "WHAT DID I SAID!! Press a,q,d or e"

def arm(): #This is the arming procedure of an ESC
    print "Connect the battery and press Enter"
    inp = input()
    if inp == '':
        pulso(ESC, 0)
        time.sleep(1)
        pulso(ESC, max_value)
        time.sleep(1)
        pulso(ESC, min_value)
        time.sleep(1)
        control()

def stop(): #This will stop every action your Pi is performing for ESC ofcourse.
    pulso(ESC, 0)
    pi.stop()

#This is the start of the program actually, to start the function it needs to be initialized before calling... stupid python.
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
    print "Thank You for not following the things I'm saying... now you gotta restart the program STUPID!!"
