screen = pygame.display.set_mode([screenWidth,screenHeight])

#Initialize Basic PyGame Components
pygame.display.init()
pygame.font.init()
pygame.init()

pygame.key.set_repeat(100,30) #Controls how held keys are repeated (delay, interval) -- See PyGame docs

clock = pygame.time.Clock() 
clock.tick(60) #Sets framerate to 60 FPS

#Allows Controller Usage
pygame.joystick.init()
controller=0 
gamepad=0
num_joysticks = pygame.joystick.get_count() #Get the current amount of connected Joysticks
if num_joysticks > 0: #If there are more than 0 joysticks
    controller = pygame.joystick.Joystick(0) 
    controller.init() #Initialize the controller
    gamepad = Controller() #Call it 'gamepad'

