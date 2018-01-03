
import time
import sys
import RPi.GPIO as GPIO


def step_8 (p):

   if p==0:
           GPIO.output(5,0)
           GPIO.output(6,0)
           GPIO.output(12,0)
           GPIO.output(13,0)

   if p==1:
           GPIO.output(5,1)
           GPIO.output(6,0)
           GPIO.output(12,0)
           GPIO.output(13,0)

   if p==2:
           GPIO.output(5,1)
           GPIO.output(6,1)
           GPIO.output(12,0)
           GPIO.output(13,0)

   if p==3:
           GPIO.output(5,0)
           GPIO.output(6,1)
           GPIO.output(12,0)
           GPIO.output(13,0)
   if p==4:
           GPIO.output(5,0)
           GPIO.output(6,1)
           GPIO.output(12,1)
           GPIO.output(13,0)
   if p==5:
           GPIO.output(5,0)
           GPIO.output(6,0)
           GPIO.output(12,1)
           GPIO.output(13,0)
   if p==6:
           GPIO.output(5,0)
           GPIO.output(6,0)
           GPIO.output(12,1)
           GPIO.output(13,1)
   if p==7:
           GPIO.output(5,0)
           GPIO.output(6,0)
           GPIO.output(12,0)
           GPIO.output(13,1)
   if p==8:
           GPIO.output(5,1)
           GPIO.output(6,0)
           GPIO.output(12,0)
           GPIO.output(13,1)
def step_4 (p):

   if p==0:
           GPIO.output(5,0)
           GPIO.output(6,0)
           GPIO.output(12,0)
           GPIO.output(13,0)

   if p==1:
           GPIO.output(5,1)
           GPIO.output(6,1)
           GPIO.output(12,0)
           GPIO.output(13,0)

   if p==2:
           GPIO.output(5,0)
           GPIO.output(6,1)
           GPIO.output(12,1)
           GPIO.output(13,0)

   if p==3:
           GPIO.output(5,0)
           GPIO.output(6,0)
           GPIO.output(12,1)
           GPIO.output(13,1)
   if p==4:
           GPIO.output(5,1)
           GPIO.output(6,0)
           GPIO.output(12,0)
           GPIO.output(13,1)


def steps_8(value):
   print value
   global pas
   if(value<0):
       for i in range (0,abs(value)):
           step_8(pas)
           time.sleep(0.005)
           pas+=1
           if(pas>=9):
              pas=1;

   else:
       for i in range (0,abs(value)):
           step_8(pas)
           time.sleep(0.005)
           if(pas==1):
              pas=9;
           pas-=1
   step_8(0)
def steps_4(value):
   print value
   global pas
   if(value<0):
       for i in range (0,abs(value)):
           step_4(pas)
           time.sleep(0.005)
           pas+=1
           if(pas>=5):
              pas=1;

   else:
       for i in range (0,abs(value)):
           step_4(pas)
           time.sleep(0.005)
           if(pas==1):
              pas=5;
           pas-=1
   step_4(0)




if __name__ == "__main__":

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(6, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)

    step_4(0)
    pas=1
    print len(sys.argv)
    if(len(sys.argv)<2):
      print ("Error en parametro")
      print ("Use: sudo python steeper.py val mode")
      print ("val = step number >0clockwise, <0 anticlockwise ")
      print ("mode = 0: 8 pasos   2: 1 paso ")
    else:
      st=int(sys.argv[1])
      if(len(sys.argv)==3 and sys.argv[2]=="1"):
         print("8 pasos")
         steps_8(st)
      else:
         print("4 pasos")
         steps_4(st)
