import pygame,sys,random,time
import math
################################################################################################################
################################## Do Not Type above this line #################################################
################################################################################################################

screenWidth = 1250
screenHeight =  700
# DO NOT ALTER THE FOLLOWING 4 LINES OF CODE
exec(compile(source=open('utility/pygame_starterMAC.py').read(), filename='pygame_starterMAC.py', mode='exec')) #Compiles and Executes the 'starterMAC' file
exec(compile(source=open('utility/pygame_setup.py').read(), filename='pygame_setup.py', mode='exec')) #Compiles and Executes the Setup File
fps = 120
clock = pygame.time.Clock()
# DO NOT ALTER THE ABOVE 4 LINES OF CODE

################################################################################################################
################################## IMAGES #################################################
################################################################################################################
player = Image("frog.png",0.1)    # Load frog.png image into player variable & set the scale to 0.1 of the original size
bug  = Image("fly.png",0.15)    # Load fly.png image into the bug variable & set the scale to 0.15 of the original size

background = Image("maze.png",1, True, screenWidth,screenHeight) #Load the maze.png image into the maze variable and set the height and width to 1250 and 700. Set transparency to TRUE.
background.x=0
background.y=0

titleScreen = Image("oilrig.png",1, False, screenWidth,screenHeight)  #Load oilrig.png into the titleScreen variable, override the scale with screenWidth and screenHeight. Transparency is FALSE for this image.
titleScreen.x=0
titleScreen.y=0

gamelogo = Image("oilrushlogo.png",1.5)
gamelogo.x = 300 
gamelogo.y = 40

pganimation = SpriteSheet("pglogo.png",5,9,1,18,0)
pganimation.x = 60
pganimation.y = 400

################################################################################################################
################################## COLORS and SOUNDS ###########################################################
################################################################################################################
frogsound = SoundEffect("croak.wav")

#Use the next 2 lines for music as you can stop, play, pause and unpause these.     https://www.pygame.org/docs/ref/music.html#module-pygame.mixer.music
#pygame.mixer.music.load("sounds//sos.mp3")     
#pygame.mixer.music.play()
                            
################################################################################################################
################################## VARIABLES ###################################################################
################################################################################################################

level = 0
score = 0
gameOver = False
name =  "Mr.Renton"

# colorName = (R,G,B)
# RGB colors :   https://www.rapidtables.com/web/color/RGB_Color.html
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
PINK = (255,20,147)
BROWN = (150,75,0)
ORANGE = (255,165,0)

################################################################################################################
######## Main Program Loops ~60x per second #####################################################################
################################################################################################################
keys_pressed = pygame.key.get_pressed()

while gameOver == False:
    ######## Leave the next 10 lines alone - DO NOT CHANGE ########
    clock.tick(fps)
    for event in pygame.event.get(): 
        keys_pressed = pygame.key.get_pressed() 
        if event.type == pygame.QUIT:
            gameOver = True
            pygame.quit()
            sys.exit()
  
    pygame.display.update()

    ################################################################################################################
    ######## LEVEL 0 - TITLE SCREEN ################################################################################
    ################################################################################################################
    if level == 0 : #indented to column 4
        screen.fill(WHITE)
        titleScreen.display()
        gamelogo.display()
        showText("Press Enter to Start",PINK,400,300,42)    
        showText("Created by "+name,ORANGE,600,650,48)
        pganimation.display()
        
        if keys_pressed[pygame.K_RETURN]:
            level = 1 # change to level 1 from level 0

            # Reset variables at the start of a new game
            score = 0
            player.x=400
            player.y=225
            bug.x=250
            bug.y=225

    ################################################################################################################
    ######## LEVEL 1 ####### #######################################################################################
    ################################################################################################################
    if level == 1: 
        screen.fill(GREEN)
        background.display()
        player.display()
        bug.display()
        showText("Flies eaten "+str(score),YELLOW, 900, 10,36)
             
        if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
            player.x += 2
        
        if score >= 20:
            level = 1.5

    ######## LEVEL 1.5 ####### #######################################################################################
    if level == 1.5: 
        screen.fill(BLUE)
        showText("YOU WIN",YELLOW, 400, 250,72)
        showText("Press space to go next level",YELLOW, 400, 350,36)
        
        if keys_pressed[pygame.K_SPACE]:
             level = 2    

    ######## LEVEL 1.6 ####### #######################################################################################
    if level == 1.6: 
        screen.fill(RED)
        showText("YOU LOSE",YELLOW, 400, 250,72)
        showText("Press space to restart",YELLOW, 400, 350,36)
        if keys_pressed[pygame.K_SPACE]:
             level = 0   

    ################################################################################################################
    ######## LEVEL 2 ####### #######################################################################################
    ################################################################################################################
    if level == 2: 
         screen.fill(GREEN)

