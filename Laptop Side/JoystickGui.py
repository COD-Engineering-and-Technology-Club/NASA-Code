import pygame

#define colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

#this is a class for writing text to the screen
class TextPrint:
    def __init__(self, window):
        self.reset()
        self.font = pygame.font.Font(None, 20)
        self.screen = window

    def blit(self, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        self.screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height
        
    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15
        
    def indent(self):
        self.x += 10
        
    def unindent(self):
        self.x -= 10
    
#initialize pygame
pygame.init()
 
#set the width and height of the screen [width,height]
size = [500, 700]
screen = pygame.display.set_mode(size)
#set window caption
pygame.display.set_caption("GUI")

#Loop until the user exits
running = True

#set how fast program updates
clock = pygame.time.Clock()
clock_speed = 20

# Initialize the joysticks
pygame.joystick.init()
    
#create TextPrint object to write to screen
printer = TextPrint(screen)

while running:
    #check for user input
    for event in pygame.event.get(): 
    #if user clicked X
        if event.type == pygame.QUIT:
        #end program
            running = False
            
 
    #clear the screen and reset printer
    screen.fill(WHITE)
    printer.reset()

    #get count of joysticks
    joystick_count = pygame.joystick.get_count()

    printer.blit("Number of joysticks: {}".format(joystick_count) )
    printer.indent()
    
    #loop through each connected joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
    
        printer.blit("Joystick {}".format(i) )
        printer.indent()
    
        #get the name from the OS for the controller/joystick
        name = joystick.get_name()
        printer.blit("Joystick name: {}".format(name) )
        
        #get axes
        axes = joystick.get_numaxes()
        printer.blit("Number of axes: {}".format(axes) )
        printer.indent()
        
        for i in range( axes ):
            axis = joystick.get_axis( i )
            printer.blit("Axis {} value: {:>6.3f}".format(i, axis) )
        printer.unindent()

        #get buttons
        buttons = joystick.get_numbuttons()
        printer.blit("Number of buttons: {}".format(buttons) )
        printer.indent()

        for i in range( buttons ):
            button = joystick.get_button( i )
            printer.blit("Button {:>2} value: {}".format(i,button) )
        printer.unindent()
            
        #get Hat
        #value comes back in an array.
        hats = joystick.get_numhats()
        printer.blit("Number of hats: {}".format(hats) )
        printer.indent()

        for i in range( hats ):
            hat = joystick.get_hat( i )
            printer.blit("Hat {} value: {}".format(i, str(hat)) )
        printer.unindent()
        
        printer.unindent()
        
    #update display
    pygame.display.flip()

    # Limit clock speed
    clock.tick(clock_speed)

#exit pygame
pygame.quit ()