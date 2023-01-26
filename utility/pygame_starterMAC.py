
class Controller():
    def __init__(self):
        self.name = "360"

    def leftThumbX(self):
        return int(controller.get_axis(0)*10)
    
    def leftThumbY(self):
        return int(controller.get_axis(1)*10)
    
    def rightThumbX(self):
        return int(controller.get_axis(2)*10)

    def rightThumbY(self):
        return int(controller.get_axis(3)*10)

    def A(self):
        return controller.get_button(11) >0
    def B(self):
        return controller.get_button(12) >0
    def X(self):
        return controller.get_button(13) >0
    def Y(self):
        return controller.get_button(14) >0

    def leftTrigger(self):   
            return int(((((controller.get_axis(4)))+1)/2)*10  )
        
    def rightTrigger(self):
           return int(((((controller.get_axis(5)))+1)/2)*10 )


    def Xbox(self):
        return controller.get_button(10) >0
    
    def leftShoulder(self):
        return controller.get_button(8) >0
    
    def rightShoulder(self):
        return controller.get_button(9)>0
    
    def back(self):
        return controller.get_button(5)>0

    def start(self):
        return controller.get_button(4)>0

    def dpadL(self):
        return controller.get_button(2)>0

    def dpadR(self):
        return controller.get_button(3)>0
    
    def dpadU(self):
        return controller.get_button(0)>0
    
    def dpadD(self):
        return controller.get_button(1)>0

    def thumbLB(self):
        return controller.get_button(6)>0
    
    def thumbRB(Dself):
        return controller.get_button(7)>0

       
    def show(self):
    
        showText("dpad L "+str(gamepad.dpadL()),WHITE,000,000,24 )
        showText("dpad R "+str(gamepad.dpadR()),WHITE,000,50,24)
        showText("dpad U "+str(gamepad.dpadU()),WHITE,00,100,24 )
        showText("dpad D "+str(gamepad.dpadD()),WHITE,00,150,24)
        
        showText("L thumb x "+str(gamepad.leftThumbX()),WHITE,00,250,24 )
        showText("L thumb y "+str(gamepad.leftThumbY()),WHITE,00,300,24)
        
        showText("R thumb x "+str(gamepad.rightThumbX()),WHITE,00,400,24)
        showText("R thumb y "+str(gamepad.rightThumbY()),WHITE,00,450,24)
        
        showText("A button "+str(gamepad.A()),BLACK,400,000,24)
        showText("B button "+str(gamepad.B()),BLACK,400,50,24)
        showText("X button "+str(gamepad.X()),BLACK,400,100,24)
        showText("Y button "+str(gamepad.Y()),BLACK,400,150,24)

        showText("L shoulder "+str(gamepad.leftShoulder()),BLACK,400,200,24)
        showText("R shoulder "+str(gamepad.rightShoulder()),BLACK,400,250,24)
        
        showText("Back "+str(gamepad.back()),WHITE,300,300,24)
        showText("Start "+str(gamepad.start()),WHITE,300,350,24)
        showText("XBOX "+str(gamepad.Xbox()),WHITE,300,400,24)


        showText("Thumb L (button) "+str(gamepad.thumbLB()),WHITE,300,500,24)
        showText("Thumb R (button) "+str(gamepad.thumbRB()),WHITE,300,550,24)

        showText("Lft trigger "+str(gamepad.leftTrigger()),WHITE,00,500,24)
        showText("Rt trigger "+str(gamepad.rightTrigger()),WHITE,00,550,24)

class SoundEffect:
    def __init__(self, name, volume=1):
        self.audioFile = pygame.mixer.Sound("sounds//"+name)
        self.audioFile.set_volume(volume)
    def isPlaying(self): #SD Added Nov 3 2022 - Checks to see if a soundEffect is currently playing
        return self.audioFile.get_num_channels() > 0
    def Play(self, timesToPlay=1):        
        if not self.isPlaying(): #Checks to see if the sound is already playing before playing the sound
            self.audioFile.play(timesToPlay-1)
    def Stop(self):
        self.audioFile.stop()
    
class Image:
    def __init__(self, name, scale = 1,transparent=True, width=-1, height=-1 ):
        if transparent == True:
            #Note that load returns a surface, which we then convert to a bitmap 
            self.pic = pygame.image.load("images//"+name).convert_alpha() #Converts the surface to a bitmap w/transparency for blitting
        else:
            self.pic = pygame.image.load("images//"+name).convert() #Converts the surface to a bitmap without transparency

        self.pic2=self.pic
        self.angle = 0
        self.angle2= 0
        self.x = 0
        self.y = 0
        self.scale = scale
        self.setScale(scale)
        self.flip = False
        if (width > 0 and height > 0):
            self.pic = pygame.transform.scale(self.pic, (width, height))   
            self.width=width
            self.height=height
        self.blitRot = False
        self.rect = self.getRect()

    def flipme(self, flip = False):
        if self.flip: #If the picture is already flipped
            if not flip: #And the passed in flip is false
                self.pic = pygame.transform.flip(self.pic, True, False) #Unflip the image
        else: #If the picture has not been flipped
            if flip: #And the passed in flip is true 
                self.pic = pygame.transform.flip(self.pic, True, False) #Flip the image

        self.flip = flip #Assign the passed in flip to the image
            
    def getPic(self):
        return self.pic #Returns the image file being used by the Image

    def display(self):      
        #screen.blit(self.pic,[self.x,self.y ])
        #screen.blit(self.pic,self.getRect())
        #if not self.blitRot:
        self.rect = self.getRect()
        #else:
        #    self.blitRotate()
        screen.blit(self.pic,self.rect)
    def get_width(self):
        return self.width

    def get_height(self)  :
        return self.height
    def getRect(self):
        if not self.blitRot:
            r = pygame.Rect(self.x,self.y,self.width,self.height)
        else:
            self.blitRotate()
            r=self.rect
        
        #r.center = (self.x+math.floor(self.width/2), self.y+math.floor(self.height/2))
        return r
    
    def changePicture(self,name, scale=1, transparent=True):
        if transparent == True:
            self.pic = pygame.image.load("images//"+name).convert_alpha()
        else:
            self.pic = pygame.image.load("images//"+name).convert()
        self.pic2=self.pic
        self.setScale(scale)
        self.flip = False
        
    def rotate(self, angle = -10000):
        #angle %=360
        self.pic = self.pic2
        self.setScale()
        if angle > -10000:
            self.angle=angle
        self.pic=pygame.transform.rotate(self.pic, self.angle)
        self.blitRot=False
        
    def rotate2(self, angle = -10000):
        if angle > -10000:
            self.angle = angle
        self.blitRot=True

    def blitRotate(self, angle = -10000):
        if angle > -10000:
            self.angle = angle

        self.blitRot=True

        # calcaulate the axis aligned bounding box of the rotated image
        #w, h       = image.get_size()
        box        = [pygame.math.Vector2(p) for p in [(0, 0), (self.width, 0), (self.width, -self.height), (0, -self.height)]]
        box_rotate = [p.rotate(self.angle) for p in box]
        min_box    = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
        max_box    = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

        # calculate the translation of the pivot 
        pivot        = pygame.math.Vector2(self.width//2, -self.height//2)
        pivot_rotate = pivot.rotate(self.angle)
        pivot_move   = pivot_rotate - pivot

        # calculate the upper left origin of the rotated image
        origin = (self.x - self.width//2 + min_box[0] - pivot_move[0], self.y - self.height//2 - max_box[1] + pivot_move[1])

        if self.angle != self.angle2:
            self.angle2=self.angle

            image = pygame.transform.scale(self.pic2, (self.width, self.height))
            image = pygame.transform.rotate(image, self.angle)

            self.pic = image

        # rotate and blit the image
        #screen.blit(image, origin)

        #self.rect = (*origin, *image.get_size())
        #screen.blit(image, self.rect)

        self.rect = pygame.Rect(origin[0],origin[1],self.pic.get_size()[0],self.pic.get_size()[1])
        # draw rectangle around the image
        #pygame.draw.rect (screen, (255, 0, 0), self.rect,2)

            
        
    def changeSize(self, width=100, height=100):
        self.pic = self.pic2
        self.pic = pygame.transform.scale(self.pic, (width, height)) 
        self.width=width
        self.height=height
        self.flip = False

    def setScale(self, ratio = -10000):
        self.pic = self.pic2
        if ratio>-10000: self.scale = ratio
        temprect = self.pic.get_rect()
        self.width = (int)(temprect.width*self.scale)
        self.height = (int)(temprect.height*self.scale)
        self.pic = pygame.transform.scale(self.pic, (self.width, self.height))
        self.flip = False


class SpriteSheet:
    def __init__(self, filename, cols, rows, scale = 1, fps = 12, loops=0):
            self.sheet = pygame.image.load("images//"+filename).convert_alpha()
            self.scale = scale
            self.cols = cols
            self.rows = rows
            self.totalCellCount = cols * rows
            self.x = 0
            self.y = 0
            self.w = 0
            self.h = 0
            self.frame = 0
            if fps>0:
                self.fps = fps
                self.frameLength = 1000/self.fps
            else:
                self.fps = 0
                self.frameLength = 0
            self.timeStart = pygame.time.get_ticks()		
            self.sheet2 = self.sheet
            self.setScale(self.scale)
            self.timesToPlay = loops
            self.loopcount = 0
            self.flip = False
      
    def setScale(self, ratio = 1.5):
            self.sheet = self.sheet2
            self.scale = ratio
            self.rect = self.sheet.get_rect()
            width = (int)(self.rect.width*ratio)
            height = (int)(self.rect.height*ratio)
            self.sheet = pygame.transform.scale(self.sheet, (width, height))
            self.w = self.cellWidth = math.floor(width / self.cols)
            self.h = self.cellHeight = math.floor(height / self.rows)
            #self.cellCenter = (self.w / 2, self.h / 2)
            self.cells = list([ ( (index % self.cols) * self.w, math.floor(index / self.cols) * self.h, self.w, self.h ) for index in range(self.totalCellCount) ])
            self.rect = self.getRect()

    def setFPS(self, fps = 12):
        if fps>0:
            self.fps = fps
            self.frameLength = 1000/self.fps
        else:
            self.fps=0
            self.frameLength=0

    def setFrame(self, framenum=0):
        self.frame = framenum

    def getPic(self):
       # cellpic = screen.blit(self.sheet, (self.x, self.y), self.cells[self.frame])
       # cellpic = pygame.transform.subsurface(self.sheet, (1,1,10,10))
        cellpic = pygame.Surface((self.w,self.h), pygame.SRCALPHA)
        #cellpic.set_alpha(0)
        #BLACK = (0, 0, 0)
        #cellpic.set_colorkey(BLACK)
        #cellpic.blit(self.sheet, (0, 0), ((index % self.cols) * self.w, 0, self.w, self.h))
        if self.frame < self.totalCellCount: 
            cellpic.blit(self.sheet, (0, 0), self.cells[self.frame])
            if self.flip:
                cellpic = pygame.transform.flip(cellpic, True, False)

        #screen.blit(cellpic,[0,0])
        return cellpic

    def getRect(self):
        r = pygame.Rect(self.x,self.y,self.w,self.h)
        return r

    def play(self, x = -1, y = -1, loops = -1):
        self.frame = 0
        self.loopcount = 0
        if x>-1: self.x = x
        if y>-1: self.y = y
        if loops>-1: self.timesToPlay = loops
    
    def display(self):
        if pygame.time.get_ticks()-self.timeStart > self.frameLength and self.fps>0:
            self.frame += 1
            self.timeStart = pygame.time.get_ticks()
        if self.frame >= self.totalCellCount: 
            if self.timesToPlay == 0 or self.loopcount < self.timesToPlay-1:        
                self.loopcount +=1
                self.frame = 0
                if not self.flip:
                    screen.blit(self.sheet, (self.x, self.y), self.cells[self.frame])
                else:
                    temp_pic = self.getPic()
                    screen.blit(temp_pic, (self.x, self.y))
        else:
            if not self.flip:
                screen.blit(self.sheet, (self.x, self.y), self.cells[self.frame])
            else:
                temp_pic = self.getPic()
                screen.blit(temp_pic, (self.x, self.y))

        self.rect = self.getRect()
               
       

def imagesCollide(pic1,pic2) :
    pic1_rect = pic1.getRect()
    pic2_rect = pic2.getRect()

    overlap = pic1_rect.colliderect(pic2_rect)

    if overlap:
        if (pic1_rect.width * pic1_rect.height < pic2_rect.width * pic2_rect.height):
            pcell = pygame.Surface((pic1_rect.width, pic1_rect.height), pygame.SRCALPHA)
            pcell.blit(pic2.getPic(), (0, 0), pygame.Rect(pic1_rect.x-pic2_rect.x,pic1_rect.y-pic2_rect.y,pic1_rect.width, pic1_rect.height))

            pic1_mask = pygame.mask.from_surface(pic1.getPic())   
            pic2_mask = pygame.mask.from_surface(pcell)
        else:
            pcell = pygame.Surface((pic2_rect.width, pic2_rect.height), pygame.SRCALPHA)
            pcell.blit(pic1.getPic(), (0, 0), pygame.Rect(pic2_rect.x-pic1_rect.x,pic2_rect.y-pic1_rect.y,pic2_rect.width, pic2_rect.height))

            pic1_mask = pygame.mask.from_surface(pcell)
            pic2_mask = pygame.mask.from_surface(pic2.getPic())   

        overlap = pic2_mask.overlap(pic1_mask, (0,0))
        
    return overlap

def typetext(text):
    if event.type == pygame.KEYDOWN:
              #  if active:
                    if event.key == pygame.K_RETURN:
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
    return text

def showText(stuff,color,x,y,size):
    myFont = pygame.font.SysFont("Calibri",size,True,False)
    text = myFont.render(stuff,True,color)
    screen.blit(text,[x,y])

def mouseClick(image):

    #Note this method is implemented in a bad way according to PyGame Documentation.
        #Instead, we should be checking all events every frame, and looking for the MOUSEDOWN event
        #event.type == MOUSEBUTTONDOWN
    mousePosition = pygame.mouse.get_pos() #Returns a tuple containing the x and y position of the mouse
    imageRectangle = image.getRect() #Get the rectangle containing the image
    mouseState = pygame.mouse.get_pressed() #Returns a tuple of 3 booleans for (left, middle, right)
    return imageRectangle.collidepoint(mousePosition[0],mousePosition[1]) and mouseState[0] #Return if the mouse clicked the image



