#Nasa-bot drive code written in pygame
import time
import socket
import pygame

"""Packet Meanings:
	DR = Drive
	ST = Steer(Actuator)
	AU = Auger
	TI = Tilt(Actuators)
	SL = BallsScrew Slide
	CO = Conveyor
	"""

def stop():
        pygame.joystick.quit()
        pygame.quit()
        print("Clean exit")
        exit(0)

def main():
    print("main")
    #Control upadate frequency
    CLOCK = pygame.time.Clock()
    clock_speed = 20

    #vars for if joystick is connected and program is running
    joystick_connect = True
    running = True

    #Establish socket connections	
    HOST='192.168.1.18'
    PORT=9500
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print("Connection to " + HOST + " was successful")

    pygame.init()
    #use first joystick connected since only
    #one xbox remote is used
    joystick = pygame.joystick.Joystick(0)
    print("joystick")
    #initailize joystick
    joystick.init()
    
    while(running):
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYAXISMOTION:

                #Steering command on the top left axis left and right direction
                if joystick.get_axis(0) > .1 or joystick.get_axis(0) < -.1:
                    pwm = (joystick.get_axis(0) + 1) / .02
                    pwm = round(pwm,0)
                    if pwm > 90:
                        pwm = 90.0
                    elif pwm < 10:
                        pwm = 10.0
                    msg = "ST" + str(pwm)
                    print(msg)
                    data = msg.encode()
                    s.send(data)

                #Conveyor Belt control using the X button
                if joystick.get_button(2) != 0:
                    pwm = 90.0
                    msg = "CO" + str(pwm)
                    print(msg)
                    data = msg.encode()
                    s.send(data)

                #Auger control using the A button
                if joystick.get_button(0) != 0:
                    pwm = 10.0
                    msg = "AU" + str(pwm)
                    print(msg)
                    send = msg.encode()
                    s.send(send)
                
                #Auger control using B button
                if joystick.get_button(1) != 0:
                    pwm = 90.0
                    msg = "AU" + str(pwm)
                    print(msg)
                    send = msg.encode()
                    s.send(send)
                
                #Ballscrew slide using the left trigger
                if joystick.get_axis(2) > .5:
                    pwm = 70
                    msg = "SL" + str(pwm)
                    print(msg)
                    send = msg.encode()
                    s.send(send)

                #Ballscrew slide using right trigger
                if joystick.get_axis(2) < -.5:
                    pwm = 30
                    msg = "SL" + str(pwm)
                    print(msg)
                    send = msg.encode()
                    s.send(send)

                #Tilt using left bumper
                if joystick.get_button(4) != 0:
                    pwm = 10.0
                    msg = "TI"+str(pwm)
                    print(msg)
                    send = msg.encode()
                    s.send(send)

                #Tilt using right bumper
                if joystick.get_button(5) != 0:
                    pwm = 90.0
                    msg = "TI"+str(pwm)
                    print(msg)
                    send = msg.encode()
                    s.send(send)
                
                #Drive command using top left stick up and down
                if joystick.get_axis(1) <-.1 or joystick.get_axis(1) > .1:
                    pwm = (joystick.get_axis(1) + 1) / .02      
                    pwm = round(pwm,0)
                    if pwm > 90:
                        pwm = 90.0
                    elif pwm < 10:
                        pwm = 10.0
                    msg = "DR" + str(pwm)
                    print(msg)
                    send = msg.encode()
                    s.send(send)

                #Exit program if start button is pressed
                if joystick.get_button(7):
                    running = False

    print("Stopping")
    s.close()
    stop()
main()
