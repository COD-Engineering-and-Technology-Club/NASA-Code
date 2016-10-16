import Rpi.GPIO as GPIO

if __name__ == '__main__':

    #generic call back
    def controlCallBack(xboxControlId, value):
        print "Control Id = {}, Value = {}".format(xboxControlId, value)

    #specific callbacks for the left thumb (X & Y)
    def leftThumbX(xValue):
        print "LX {}".format(xValue)
    def leftThumbY(yValue):
        print "LY {}".format(yValue)

    #setup xbox controller, set out the deadzone and scale, also invert the Y Axis (for some reason in Pygame negative is up - wierd! 
    xboxCont = XboxController(controlCallBack, deadzone = 30, scale = 100, invertYAxis = True)

    #setup the left thumb (X & Y) callbacks
    xboxCont.setupControlCallback(xboxCont.XboxControls.LTHUMBX, leftThumbX)
    xboxCont.setupControlCallback(xboxCont.XboxControls.LTHUMBY, leftThumbY)
	xboxCont.setupControlCallback(
        	xboxCont.XboxControls.A,
        	c1Callback)
		xboxCont.start()
	while True:
        	time.sleep(.1)

	xboxCont.stop()

