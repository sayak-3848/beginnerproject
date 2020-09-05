import pygame#importing the pygame module
pygame.init()#pyagme module initialized.

#screen(window on which we need to draw on)
screen = pygame.display.set_mode((800, 480))#length and width of the screen(x, y) coordinates form
pygame.display.set_caption("First Game")#set the caption of the screen(window)
bg = pygame.image.load('bg.jpg') #load the background image.
char = pygame.image.load('standing.png') #load the standing image on the screen(when it stops then the player stand and look at us)

clock = pygame.time.Clock() #create a clock object to help track an amount of time.

bulletSound = pygame.mixer.Sound("C:/Users/HP/Documents/pygame/bulletbody.wav")#create a new sound object from a file.
hitSound = pygame.mixer.Sound("C:/Users/HP/Documents/pygame/htisound.wav") #create a new sound object from a file.
music = pygame.mixer.music.load('C:/Users/HP/Documents/pygame/backgroundmusic.mp3') #load a music file for playback.
pygame.mixer.music.play(-1) #start the playback of the music stream.(-1 is to play the music indefinitely many times)
score = 0

#Player description
class Player(object):#create a class for player (to make a player datatype)
    #sequential images of the player turning to right.
    walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'),
             pygame.image.load('R6.png'),pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
    #sequential images of player turning to left.
    walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'),
            pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
    #this is called initialization function
    def __init__(self, x, y, width, length):#this function for the attribute of the player class.
        self.x = x #x-coordinate of the player(to set the location)
        self.y = y #y-coordinate of the player(to set the location)
        self.width = width #width of the player
        self.length = length #length of the player
        self.velocity = 8 #the speed with which the object moves
        self.left = False #initially not turning to left (so the variable is set to False)
        self.right = True #initially turning to right (so the variable set to True)
        self.walkCount = 0 #initially the walkcount of the player is set to 0(cause do not move in the beginning)
        self.is_jump = False #initially the player wont be jumping.
        self.jumpcount = 10 #the number of jumps made by the object.
        self.standing = True #initially the player will be just standing staring at us so it set to True.
        #a hitbox that surrounds the player.
        self.hitbox = (self.x + 17, self.y + 2, 31, 57) #hitbox = (x, y, width, height)

    def draw(self): #this function defined to draw the player on the screen
        if self.walkCount + 1 >= 27: #27 means = 3 frames per each sprite, it is going out of the screen.
            self.walkCount = 0 #as it is going out off the screen then the walkcount set to 0.
        if not(self.standing): #if the player is not standing
            if self.left: #then if it moves left.
                screen.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))#draw all the images on the screen in a sequence.
                self.walkCount += 1 #walkcounts incremented by 1 
            elif self.right: #or else move to the right
                screen.blit(self.walkRight[self.walkCount//3], (self.x,self.y)) #draw all the images on the screen in a sequence.
                self.walkCount += 1 #walkcounts incremented by 1.
        else: #if the player is standing
            if self.right: #in the right direction 
                screen.blit(self.walkRight[0], (self.x, self.y))#looking in the right direction as if it is about to move to the right
                #instead of the standing still staring at us.
            else: #in the left direction
                screen.blit(self.walkLeft[0], (self.x, self.y))#looking in the left direction as if it is about to move to the left.
                #instead of standing and staring at us.

        self.hitbox = (self.x + 17, self.y + 12, 29, 52) #and this is the dimension of the hitbox.
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)#drawing the rectangle around the player with 2 width gap.

    def hit(self): #this function is defined to make sure when the player gets hit.
        self.is_jump = False
        self.jumpcount = 10
        self.x = 60
        self.y = 410
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, (255,0,0))
        screen.blit(text, (250 - text.get_width()//2, 200))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.wait(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
                
class Projectile(object):
    def __init__(self, x, y, color, radius, facing):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.facing = facing
        self.velocity = 10 * facing

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

class Enemy(object):# this class is being created for the enemy datatype
    #sequential images of the enemy turning right
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'),
                 pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'),
                 pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    #sequential images of the enemy turning left.
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'),
                pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'),
                pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]
    #initialization function for the enemy.
    def __init__(self, x, y, width, length, end):#this function to set the attribute for the enemy
        self.x = x #x-coordinate of the enemy(to set the location)
        self.y = y #y-coordinate of the enemy(to set the location)
        self.width = width #width of the enemy.
        self.length = length #length of the enemy
        self.end = end #this is the ending point where the enemy stops (as enmey is moving on its own)
        self.path = [self.x, self.end]#this is to determine where it starts and where it ends.
        self.walkCount = 0 #initially the walkcount set to 0.(as do not move in the beginning)
        self.velocity = 8 #at what speed the enemy is moving on the screen.
        self.hitbox = (self.x + 17, self.y + 2, 31, 57) #(x, y, width, height)
        self.health = 9 #the health bar of the enemy 
        self.visible = True #initially the enemy will be visible on the screen.

    def draw(self):# the function is to draw the enmey on the screen
        self.move()
        if self.visible: #when the enemy is visible on the screen.
            if self.walkCount + 1 >= 33: #33 means = 3 frames per each sprite.
                self.walkCount = 0 #then going out of the screen, which means no more walkcounts.

            if self.velocity > 0: #it means moving to the right.
                screen.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))#draw the images of moving to the right in a sequence.
                self.walkCount += 1 #walkcount is incremneted by 1

            else: #moving to the left.
                screen.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y)) #draw images of moving to the left in a sequence.
                self.walkCount += 1 #walkcount is incremented by 1.
  
        pygame.draw.rect(screen, (255, 0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
        pygame.draw.rect(screen, (255, 255,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10)) 
        
        self.hitbox = (self.x + 17, self.y + 2, 31, 57) #The dimension of the hitbox.
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2) #drawing the rectangular hitbox around the enemy.

    def move(self):#this function is defined to make sure the enemy is moving on the screen.
        if self.velocity > 0:
            if self.x + self.velocity < self.path[1]:
                self.x += self.velocity
            else:
                self.velocity = self.velocity * -1
                self.walkCount = 0
        else:
            if self.x - self.velocity > self.path[0]:
                self.x += self.velocity
            else:
                self.velocity = self.velocity * -1
                self.walkCount = 0

    def hit(self):#this function is to make sure whether the enemy is hit or not.
        if self.health > 0: #if the self.health is greater than 0 and it gets hit with bullet
            self.health -= self.health #then health of the enemy decreases by 1
        else: #and if health is equal to 0
            self.visible = False #then the enemy becomes invisible.
        print("BOOM") #print the statement when the enemy gets hit by the bullet.

#this is an independent function, not under any class
def redrawGameWindow(): #this function is being defined to draw all the stuffs(bg, player, enemy, text) everything.
    #blit function is draw the image on the screen
    screen.blit(bg, (0,0))#to draw the background image on the screen.
    text = font.render("Score: " + str(score), 1, (0,0,0))
    screen.blit(text, (350, 10))#to draw the text on the screen
    man.draw() # to draw the player on the screen by calling out the function.
    goblin.draw() #to draw the enemy on the screen by calling out the function.
    for goli in bullets: #
        goli.draw() 
    pygame.display.update() #to update the screen.

#instances of the classes.
man = Player(80, 410, 64, 64) #instances of the player class
goblin = Enemy(100, 410, 64, 64, 500) #instance of the enemy class
shootLoop = 0

font = pygame.font.SysFont("comicsans", 30, True)

#Main loop(to be persistnet)
#make things continuously appears
running = True#variable called for the things to be persistent
bullets = []
while running:#make an infinite loop(while loop is best for infinite loop)
    #funtion of the clock object to set the framerate.
    clock.tick(27) #this is the framerates per second.
    
    if goblin.visible == True:
        if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[1] > goblin.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                man.hit()
                score = score - 5

        if shootLoop > 0:
            shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0
        
    for event in pygame.event.get():#this method gives you the list of events happened by the user.(for loop to iterate over the loop)
        #To grab the specific events from the stack(list) of events by the type method.
        if event.type == pygame.QUIT:#when the type of event is pressing the red cross button
            running = False#then the program ends and the screen closes.

    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                hitSound.play()
                goblin.hit()
                score = score + 1
                bullets.pop(bullets.index(bullet))
                
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()#this gives you the state of all the buttons in the keyboard.(list of all buttons)
    #to shoot bullets on the enemy(goblin)
    if keys[pygame.K_SPACE] and shootLoop == 0:
        bulletSound.play()
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 2:
            bullets.append(Projectile((man.x + man.width // 2), (man.y + man.length // 2), (0,0,0), 4, facing))


        shootLoop = 1
    #To move Left (negative x)    
    if keys[pygame.K_LEFT] and man.x > (0 + man.velocity):#when you press the left key button and the x greater than 0
        man.x -= man.velocity#then moves to the left with a certain velocity given in the attribute.
        man.left = True #it only moves to the left.
        man.right = False #but can not move to the right, so it is set to false
        man.standing = False #it is not standing right now because it is moving to the left.(so it is set to False)
    #To move right(positive x)
    elif keys[pygame.K_RIGHT] and man.x < 800 - (man.width + man.velocity):#when you press the right key and the x less than the given condition.
        man.x += man.velocity#then moves to the right with a certain velocity given in the attribute
        man.right = True#it only moves to the right.
        man.left = False#but can not moves to the left, so it is set to false.
        man.standing = False #it is not standing right now because it is moving in the right direction.
    #moving in no direction
    else:#neither right nor left.
        man.standing = True #so the mna is in standing position and staring at us
        man.walkCount = 0 # and as it is not moving so the walkcount is set to 0.

    if not man.is_jump: #when the player is not jumping then the below conditions will play.
        if keys[pygame.K_UP]: #when you press the up direction button 
            man.is_jump = True #then the player jump(so it is set True)
            man.left = False #the object not moving left(the object can not move to the left while it is jumping) so set to False.
            man.right = False #neither it is moving right (the object can not move to the right while it is jumping) so set to False.
            man.walkCount = 0 #it is jumping but it is not walking, so the walkcount is set to zero.
    #when we hit the space button.
    else: #when the man is jumping.
        if man.jumpcount >= -10:#when the jumpcount is more than or equal to -10.
            neg = 1 #and setting a variable to 1(always we do that). 1 will get you to the surface.
            if man.jumpcount < 0: #and the jumpcount is a negative value
                neg = -1 #then reset the variable to -1 and then the complete process.
            #as we are moving up so negative y, and squaring because to move up.
            #it is a lot of pixels we will not moving that much so we subtract by 2.
            #and at last to return to the surface again we are multiplying with negative value.
            #so that negative negative changes to positive.
            man.y = man.y - (man.jumpcount ** 2) // 2 * neg #this is the quadratic equation to for the jump.
            man.jumpcount = man.jumpcount - 1 #this is to reduce the jumpcount every time by 1.
        
        else: #when the jump has concluded
            man.is_jump = False #then the man is no longer jumping so the variable is set to False.
            man.jumpcount = 10 #the jumpcount variable is set to the initial state again.

    #Calling out the function
    redrawGameWindow() #if we do not call the function then nothing will be drawn on the screen as the function is for drawing the images on the screen.
        
pygame.quit()#the screen closes and ends the program once you click the red button.
