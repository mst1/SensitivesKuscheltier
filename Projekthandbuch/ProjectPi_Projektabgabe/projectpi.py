#Imports
import RPi.GPIO as GPIO
import socket
import os
import thread
import picamera
import time
#from TSL2561 import *

#tsl = TSL2561()

os.chdir('/usr/projectpi')

#Programmstart
print 'Software Raspberry Pi starting'
#Portkonstante
PORT = 50000;
GPIO.setmode(GPIO.BOARD)
#GPIO Sensor Numbers
LH_SELFIE = 29
RH_TASTER = 31
OHR_TASTER = 23
APRX = 35
BELLY = 33
#GPIO RGB Led
LEFT_RGB_R=7
LEFT_RGB_G=11
LEFT_RGB_B=13
RIGHT_RGB_R=15
RIGHT_RGB_G=19
RIGHT_RGB_B=21

LIGHT_VALUE=50

#GPIO_setup_Sensoren
GPIO.setup(LH_SELFIE, GPIO.IN)
GPIO.setup(RH_TASTER, GPIO.IN)
GPIO.setup(OHR_TASTER, GPIO.IN)
GPIO.setup(APRX, GPIO.IN)
GPIO.setup(BELLY, GPIO.IN)
#GPIO_setup_LEDs
GPIO.setup(LEFT_RGB_B, GPIO.OUT, GPIO.LOW)
GPIO.setup(LEFT_RGB_G, GPIO.OUT, GPIO.LOW)
GPIO.setup(LEFT_RGB_R, GPIO.OUT, GPIO.LOW)
GPIO.setup(RIGHT_RGB_B, GPIO.OUT, GPIO.LOW)
GPIO.setup(RIGHT_RGB_G, GPIO.OUT, GPIO.LOW)
GPIO.setup(RIGHT_RGB_R, GPIO.OUT, GPIO.LOW)

#Start des Servers
def init_netw():
	s = socket.socket()
	s.bind(('', PORT))
	s.listen(1)
	while True:
		c, a=s.accept()
		cmd = c.recv(1024)
        netcmd(cmd)

def playsound(sound):
	os.system("aplay "+sound)

def augenfarbe(r, g, b):
	thread.start_new_thread(augenfarbe_thread,(r, g, b))

def augenfarbe_thread(r, g, b):
	if(r==True):
		GPIO.output(LEFT_RGB_R, 1)
		GPIO.output(RIGHT_RGB_R, 1)
	else:
		GPIO.output(LEFT_RGB_R, 0)
		GPIO.output(RIGHT_RGB_R, 0)
	if(g==True):
		GPIO.output(LEFT_RGB_G, 1)
		GPIO.output(RIGHT_RGB_G, 1)
	else:
		GPIO.output(LEFT_RGB_G, 0)
		GPIO.output(RIGHT_RGB_G, 0)
	if(b==True):
		GPIO.output(LEFT_RGB_B, 1)
		GPIO.output(RIGHT_RGB_B, 1)
	else:
		GPIO.output(LEFT_RGB_B, 0)
		GPIO.output(RIGHT_RGB_B, 0)
	time.sleep(3)
	GPIO.output(LEFT_RGB_R, 0)
	GPIO.output(RIGHT_RGB_R, 0)
	GPIO.output(LEFT_RGB_G, 0)
	GPIO.output(RIGHT_RGB_G, 0)
	GPIO.output(LEFT_RGB_B, 0)
	GPIO.output(RIGHT_RGB_B, 0)

def pic():
	tmp = time.strftime("%d_%m_%Y_%H_%M_%S")
	os.system("raspistill -o /Fotos/"+tmp+".jpg")
	
def netcmd(cmd):
	if (cmd=='shutd'):
		os.system("shutdown -h now")
	elif (cmd=='killsoft'):
		RUNNING = False
	elif (cmd=='reboot'):
		os.system("reboot")
	elif (cmd=='ledred'):
		print 'Red eyes'
		augenfarbe(True, False, False)
	elif (cmd=='ledgreen'):
		print 'Green eyes'
		augenfarbe(False, True, False)
	elif (cmd=='ledblue'):
		print 'Blue eyes'
		augenfarbe(False, False, True)
	elif (cmd=='ledyellow'):
		print 'Yellow eyes'
		augenfarbe(True, True, False)
	elif (cmd=='ledmagenta'):
		print 'Magenta eyes'
		augenfarbe(True, False, True)
	elif (cmd=='ledtuerkis'):
		print 'Turkies eyes'
		augenfarbe(False, True, True)
	elif (cmd=='ledwhite'):
		print 'White eyes'
		augenfarbe(True, True, True)
	elif (cmd=='ledblank'):
		print 'Blank eyes'
		augenfarbe(False, False, False)
	else:
		print cmd
		playsound(cmd)

#Taster + Annaeherung
def LH_SELFIEM(VAR):
	print 'Left hand'
	playsound('Foto.wav')
	augenfarbe(True, True, True)
	pic()
def RH_TASTERM(VAR):
	print 'Right Hand'
	augenfarbe(True, True, False)
	playsound('Donnerblitz.wav')
def OHR_TASTERM(VAR):
	print 'Ear'
	playsound('Ear.wav')
def APRXM(VAR):
	print 'Object near'
	augenfarbe(False, True, True)
	playsound('Annaeherung.wav')
def BELLYM(VAR):
	print 'Belly'
	augenfarbe(True, False, False)
	playsound('Bauch.wav')

def softclose():
	#GPIOs freigeben
	GPIO.cleanup()
	#Programm beenden
	playsound('Ausschalten.wav')
	exit()

def light():
	if(tsl.getLuminosity(tsl.VISIBLE)<LIGHT_VALUE):
		#dunkel
		return False;
	else:
		#hell
		return True


def light_thread():
	oldvalue=light();
	while True:
		sleep(10)
		newvalue=light()
		if(oldvalue!=newvalue):
			if(newvalue):
				#Jetzt ist es hell
				playsound('Hell.wav')
			else:
				#Jetzt ist es dunkel
				playsound('Dunkel.wav')
			oldvalue=newvalue

#GPIOs start
GPIO.add_event_detect(LH_SELFIE, GPIO.RISING, callback=LH_SELFIEM);
GPIO.add_event_detect(RH_TASTER, GPIO.RISING, callback=RH_TASTERM);
GPIO.add_event_detect(OHR_TASTER, GPIO.RISING, callback=OHR_TASTERM);
GPIO.add_event_detect(APRX, GPIO.RISING, callback=APRXM);
GPIO.add_event_detect(BELLY, GPIO.RISING, callback=BELLYM);

thread.start_new_thread(init_netw,())
#thread.start_new_thread(light_thread,())

#Programm nicht anhalten
RUNNING = True
while True:
	continue

GPIO.cleanup()

#except KeyboardInterrupt:
#	GPIO.cleanup()
