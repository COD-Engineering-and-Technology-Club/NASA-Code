import XboxController
import RPi.GPIO as GPIO
import time


class InitioXboxControl:
	def __init__(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(16, GPIO.OUT)
		GPIO.setup(20, GPIO.OUT)
		GPIO.setup(21, GPIO.OUT)
		self.c1=GPIO.PWM(16, 50)
		self.c2=GPIO.PWM(20, 50)
		self.c3=GPIO.PWM(21,50)
		
		self.xValue = 0
		self.yValue = 0
		self.pwm = 0
		self.c1.start(pwm)
                self.c2.start(pwm)
                self.c3.start(pwm)


		self.xboxCont = XboxController.XboxController(deadzone = 25,
							joystickNo = 0,
							scale = 100,
							invertYAxis = True)
		self.xboxCont.setupControlCallback(self.xboxCont.XboxControls.LTRIGGER, self.c1)
		self.xboxCont.start()
		self.running = True

		def c1Funct(self, xValue):
			self.xValue = xValue
			self.updateChannel()
			print "Got to c1Func"

		def updateChannel(self):				
			print xValue
			if(self.xValue > 8000):
               			self. pwm = 100
       			elif(self.xValue > 6000):
                		self.pwm = 90
        		elif(self.xValue > 4000):
                		self.pwm = 80
        		elif(self.xValue > 2000):
                		self.pwm = 60
        		elif(self.xValue > 0):
                		self.pwm = 50
        		elif(self.xValue > -2000):
                		self.pwm = 40
        		elif(self.xValue > -4000):
                		self.pwm = 30
        		elif(self.xValue > -6000):
                		self.pwm = 20
        		elif(self.xValue > -8000):
                		self.pwm = 10
        		else:
				self.pwm=0
			
			if(pwm!=0):
				self.c1.changeDutyCycle(pwm)
				print "c1 has power"
			else:
				self.c1.stop()
				print "No power"
				self.xboxCont.stop()
if __name__ == '__main__':

    print ("started")
    try:
        #create class
        initioCont = InitioXboxControl()
        while initioCont.running:
            time.sleep(0.1)

    #Ctrl C
    except KeyboardInterrupt:
        print "User cancelled"

    #Error
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise
    
    finally:
        print 
        print ("stop")
        #if its still running (probably because an error occured, stop it
        if initioCont.running == True: initioCont.stop()
