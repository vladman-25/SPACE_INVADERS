import pygame
import sys

########### STABILESC CATEVA CULORI PE CARE LE VOI FOLOSI ##########
COLOR_BLACK = (0, 0, 0)
COLOR_GREEN = (0, 204, 0)
COLOR_BACKGROUND = (51, 0, 102)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0 ,0)

########## INCARC IMAGINILE PE CARE LE VOI FOLOSI ##############
ALIEN = pygame.image.load('IMAGES/alien2.png')
ALIEN = pygame.transform.scale(ALIEN, (50, 47))
SHIP = pygame.image.load('IMAGES/ship.png')
SHIP = pygame.transform.scale(SHIP, (70, 64))
HEART = pygame.image.load('IMAGES/heart.png')
HEART = pygame.transform.scale(HEART, (20, 20))


    
############### CLASA PRIN CARE CREEZ NAVA PRINCIPALA ########
class MyShip:

    SPEED = 3
    WIDTH = 70
    HEIGTH = 64
    
############### POZITIA INITIALA A NAVEI ##########    
    def __init__(self):
        self.x = SpaceGame.WIDTH / 2
        self.y = SpaceGame.HEIGHT - 70
        self.lifes = SpaceGame.LIVES
        
############## ACTIUNEA PT TASTA A #################
    def move_left(self):
        if self.x >= 0:
            self.x -= self.SPEED 
            
############## ACTIUNEA PT TASTA D ################       
    def move_right(self):
        if self.x + 70 <= SpaceGame.WIDTH:
            self.x += self.SPEED
            
############## INCARCAREA PE ECRAN A NAVEI LA POZITIA ACTUALA ######               
    def render(self, background):
        background.blit(SHIP, (self.x,self.y) )

############## VERIFIC COLIOZIUNEA CU GLOANTELE EXTRATERESTRE ######        
    def colision_bullets(self):
        for bullet in SpaceGame.bulletsAliens:
            if bullet.y + 25> self.y and bullet.x <= self.x + 70 and bullet.x >= self.x:
                SpaceGame.bulletsAliens.remove(bullet)
                SpaceGame.LIVES -= 1


############ CLASA PENTRU NAVELE INAMICE  #############    
class MyAlien:

    SPEED = 0.2
    WIDTH = 50
    HEIGTH = 47
    k = 101
    true = 1
    last_fire = 0
    
############ INAMICUL ESTE GENERAT LA COORDONATELE DATE ######    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.yinitial = y
        self.xinitial = x

########### REALIZEZ MISCAREA LA STANGA SAU DREAPTA ###########
    def update(self):
        self.y += self.SPEED
        if self.k > 0 and self.true ==1:
            self.x += 1
            self.k += 1
            if self.k == 200:
                self.true = 0
        else: 
            self.x -= 1
            self.k -= 1
            if self.k == 1: 
               self.true = 1

########### INCARC INAMICUL PE ECRAN ####################    
    def render(self, background): 
        self.update()
        background.blit(ALIEN, (self.x, self.y) )
    
              

######## CLASA PENTRU GLOANTELE INAMICE #################     
class AlienBullet:
    
    SPEED = 2
    WIDTH = 3
    HEIGTH = 25
    
######## GLONTUL ESTE INITIALIZAT LA COORDONATELE DATE #############
    def __init__(self, x, y):
        self.x = x
        self.y = y

####### GLONTULSE DEPLASEAZA IN JOS CU VITEZA STABILITA #####        
    def update(self):
        self.y += self.SPEED

######## INCARC GLONTUL PE ECRAN ##################    
    def render(self, background):
        self.update()
        pygame.draw.rect(background,
                         COLOR_RED,
                         pygame.Rect(self.x, self.y, self.WIDTH, self.HEIGTH))
            

######## ESTE TRAS UN GLONT DIN DREPTUL UNUI INAMIC ##########
def AlienShoot(self, posx, posy):
    
    SpaceGame.bulletsAliens.append(AlienBullet(posx,posy))
            
######## CLASA PENTRU GLOANTELE PROPRII ###########            
class MyBullet: 
    
    SPEED = 3
    WIDTH = 3
    HEIGTH = 25
    
######## GLONTUL ESTE INITIALIZAT LA COORDONATELE DATE #####  
    def __init__(self, x, y):
        self.x = x
        self.y = y

####### GLONTUL SE DEPLASEAZA IN SUS ###########        
    def update(self):
        self.y -= self.SPEED

####### GLONTUL ESTE INCARCAT PE ECRAN #########        
    def render(self, background):
        self.update()
        pygame.draw.rect(background,
                         COLOR_GREEN,
                         pygame.Rect(self.x, self.y, self.WIDTH, self.HEIGTH))
           

######### UN BUNCAR DESTRUCTIBIL ESTE CREAT DIN MAI MULTE BUCATI MAI MICI #######
######### CLASA PENTRU BUNCARE #######
class MyBunker:

    WIDTH = 100
    HEIGTH = 25
    chunks = []

######### STABILESC COORDONATELE BUNCARULUI #######    
    def __init__(self,x, y):
        self.x= x
        self.y= y
        self.count = x

######### IN FUNCTIE DE COORDONATE, SUNT CREATE BUCATILE MAI MICI DIN BUNCAR (CHUNK-URI) #######    
    def create(self):
        for y in range(self.y,self.y+15,3):
            for x in range(self.x,self.x+99,3):
                self.chunks.append(MyBunkerChunk(x, y))


######### VERIFIC COLIZIUNEA DINTRE GLOANTELE PROPRII SI BUNCAR ###########
######### IN CAZUL COLIZIUNII SE DISTRUGE CHUNK-UL LOVIT SI GLONTUL RESPECTIV #####    
    def colision_chunks(self):        
        for chunk in self.chunks:
            for bullet in SpaceGame.bullets:
                if bullet.y < chunk.y + 3 and bullet.x <= chunk.x + 3 and bullet.x >= chunk.x:
                    SpaceGame.bullets.remove(bullet)
                    self.chunks.remove(chunk)
    
######### VERIFIC COLIZIUNEA DINTRE GLOANTELE INAMICE SI BUNCAR ###########
######### IN CAZUL COLIZIUNII SE DISTRUGE CHUNK-UL LOVIT SI GLONTUL RESPECTIV #####     
    def colision_chunksAliens(self):
        for chunk in self.chunks:
            for bullet in SpaceGame.bulletsAliens:
                if bullet.y + 25 > chunk.y and bullet.x <= chunk.x + 3 and bullet.x >= chunk.x:
                    SpaceGame.bulletsAliens.remove(bullet)
                    self.chunks.remove(chunk)

######## INCARC BUNCARUL (CHUNK-URILE) PE ECRAN ###############   
    def render(self, background):
        for x in self.chunks:
            x.render(background)
            
######## CLASA PENTRU CHUNK-URI DE BUNCAR ##############
######## INITIALIZARE + INCARCARE PE ECRAN ########    
class MyBunkerChunk:
    
    WIDTH = 3
    HEIGTH = 3
    
    def __init__(self, x ,y):
        self.x = x
        self.y = y

    def render(self, background):
        pygame.draw.rect(background,
                         COLOR_WHITE,
                         pygame.Rect(self.x, self.y, self.WIDTH, self.HEIGTH))


######## VERIFIC COLIZIUNEA DINTRE INAMIC SI GLONTUL MEU ##########
def Colision(aX, aY):
    
    check = 0
    
    for bullet in SpaceGame.bullets:
        if bullet.y <= aY + 47 and bullet.x <= aX+50 and bullet.x >= aX:
            SpaceGame.bullets.remove(bullet)
            check = 1
                
    return check



########## ECRANUL GAME OVER ###############################################
def gameOverScreen(screen,SCORE,HIGHSCORE1):

########## SE AFISEAZA MESAJUL SI SCORUL ##########################
    pygame.draw.rect(screen,
                         COLOR_BACKGROUND,
                         pygame.Rect(0, 0, 800, 800))
    pygame.display.flip()
    font = pygame.font.Font('freesansbold.ttf', 50) 
    text = font.render('SCORE: ' + str(SCORE), True, COLOR_GREEN, COLOR_BACKGROUND) 
    textRect = text.get_rect()
    textRect.center = ( 400, 400)
    screen.blit(text, textRect)
    pygame.display.flip()
    
########## SE ACTUALIZEAZA HIGHSCORE-UL #########################
    my_file = open("HIGHSCORE/HIGHSCORE.txt", "w")
    my_file.write(str(HIGHSCORE1))
    my_file.close()

########## PENTRU CATEVA SECUNDE ECRANUL AFISEAZA SCORUL, APOI SE INCHIDE APLICATIA ###
    start = pygame.time.get_ticks()
    while True:
        now = pygame.time.get_ticks()
        if now - start > 2000 :
            break
    pygame.quit()
    sys.exit()

HIGHSCORE = 0    
gameover = False
run = True
###############################################################################
class SpaceGame:
    FPS = 60
    WIDTH = 800
    HEIGHT = 800
    aliens = []
    bullets = [] # TOATE GLOANTELE PROPRII
    bulletsAliens = [] # TOATE GLOANTELE INAMICE
    bunkers = [] # BUNCARE
    SCORE = 0
    last_fire1 = 0
    LIVES = 3
    ALIENCOUNT = 0
    ALIENCOUNTMAX = 0

####### EXTRAG HIGHSCORE-UL DIN FISIER #########    
    with open('HIGHSCORE/HIGHSCORE.txt', 'r') as reader:
        for line in reader:
            HIGHSCORE = line
    
    HIGHSCORE = int(HIGHSCORE)
            
    def __init__(self):
        self.ship = MyShip() # CREEZ NAVA PROPRIA
        
        
        for x in range (30, self.WIDTH-150 , 200):
            self.bunkers.append(MyBunker(x, 700)) # CREEZ BUNCARE
        for x in self.bunkers:
            x.create() # PT FIECARE BUNCAR CREEZ CHUNK-URILE SALE
        
        
        for x in range(110, self.WIDTH-140, 120):
            for y in range(5):
                self.aliens.append(MyAlien(x,y*60+10)) # CREEZ INAMICI
                self.ALIENCOUNT += 1
        self.ALIENCOUNTMAX = self.ALIENCOUNT
        
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.background = None

    def start(self):
        self.background = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.background = self.background.convert()
        self.background.fill(COLOR_BACKGROUND)
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()
                
        
        # Main loop
        last_fire= 0
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_a]:
                self.ship.move_left()
            if keys_pressed[pygame.K_d]:
                self.ship.move_right()
######################################3###################################
            if keys_pressed[pygame.K_SPACE]:
                now = pygame.time.get_ticks()
                if now - last_fire >= 400: # GLOANTELE AU UN COOLDOWN INTRE GENERARI
                    last_fire = pygame.time.get_ticks()
                    self.bullets.append(MyBullet(self.ship.x+35,self.ship.y)) # CREEZ GLOANTELE PROPRII

#############################################################################
            self.update()
            self.render()

    def update(self):
        self.clock.tick(SpaceGame.FPS)


    def render(self):
    
########## AFISEZ NR DE VIETI, SCORUL SI HIGHSCORE-UL ###########
        self.background.fill(COLOR_BACKGROUND)
               
        font = pygame.font.Font('freesansbold.ttf', 20)
    
        self.text = font.render('SCORE: ' + str(self.SCORE), True, COLOR_GREEN, COLOR_BACKGROUND) 
        self.textRect = self.text.get_rect()
        self.textRect.center = ( 700, 15)
        self.background.blit(self.text, self.textRect)       
                        
        self.text3 = font.render('HIGHSCORE: ' + str(self.HIGHSCORE), True, COLOR_GREEN, COLOR_BACKGROUND) 
        self.textRect3 = self.text3.get_rect()
        self.textRect3.center = ( 400, 15)
        self.background.blit(self.text3, self.textRect3)
        
        self.text2 = font.render(str(self.LIVES) +  ' x ', True, COLOR_GREEN, COLOR_BACKGROUND) 
        self.textRect2 = self.text2.get_rect()
        self.textRect2.center = ( 40, 15)
        self.background.blit(self.text2, self.textRect2) 
        self.background.blit(HEART, (60, 2))
        
#########################################################################   
        self.ship.render(self.background) #UPDATARE NAVA PE ECRAN
        self.ship.colision_bullets() #VERIFICARE COLIZIUNILOR NAVA-GLONT

####### DACA INAMICII INITIALI SUNT DISTRUSI, SUNT GENERATI O SERIE NOUA ###        
        if self.ALIENCOUNT == 0: 
            for x in range(110, self.WIDTH-140, 120):
                for y in range(5):
                    self.aliens.append(MyAlien(x,y*60+10))
                    self.ALIENCOUNT += 1
        
        
        
        
####### UPDATARE BUNCARE ###########       
        for x in self.bunkers: 
            x.colision_chunks()
            x.colision_chunksAliens()           
            x.render(self.background)

###### VERIFICARE COLIZIUNE INAMICI-GLONT + SCOR #######        
        for alien in self.aliens:
            a = Colision(alien.x, alien.y)
            if a==1 :
                self.aliens.remove(alien)
                self.SCORE += 5
                self.ALIENCOUNT -= 1

##### UPDATARE HIGHSCORE DACA ESTE DEPASIT #########        
        if self.HIGHSCORE < self.SCORE:
            self.HIGHSCORE = self.SCORE

##### STERGEREA GLOANTELOR DACA DEPASESC ECRANUL #####        
        for bullet in self.bullets:
            if bullet.y < 0:
                self.bullets.remove(bullet)

##### UPDATARE INAMICI + DACA INAMICII TREC DE PARTEA DIN JOS A ECRANULUI = GAME OVER ###        
        for x in self.aliens:
            x.render(self.background)
            if(x.y > 750):
                gameOverScreen(self.screen,self.SCORE,self.HIGHSCORE)

##### UPDATARE GLOANTE PROPRII ##########                 
        for x in self.bullets:
            x.render(self.background)



####################################################################################
########## ALIENII CEI MAI APROAPE DE NAVA DE PE FIECARE COLOANA TRAG GLOANTE ######
########## EXISTA UN COOLDOWN INTRE FIECARE TRAGERE ################################

        now1 = pygame.time.get_ticks()
        if now1 - self.last_fire1 >= 2000:
            for x in range(110, self.WIDTH-140, 120):
                minim = 999
                minimy = 0
                check = 0
                for alien in self.aliens:
                    if alien.xinitial == x:
                        if abs(alien.y - self.ship.y) < minim:
                            minim = abs(alien.y - self.ship.y)
                            minimx = alien.x
                            minimy = alien.y
                        check = 1
                if check == 1:
                    AlienShoot(self,minimx+25,minimy+50)
            self.last_fire1 = pygame.time.get_ticks() 

########### DACA GLOANTELE DEPASESC DIMENSIUNILE ECRANULUI, ELE SE STERG #########        
        for bullet in self.bulletsAliens:
            if bullet.y > 800:
                self.bulletsAliens.remove(bullet)
                
########## UPDATARE GLOANTE INAMICE #############################################
        for x in self.bulletsAliens:
            x.render(self.background)
###################################################################        
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

########## DACA RAMAI FARA VIETI = GAME OVER #################        
        if self.LIVES == 0:
            gameOverScreen(self.screen,self.SCORE,self.HIGHSCORE)



###############################################################################
def main():
    global run, gameover
    # Initialize imported pygame modules
    pygame.init()

    # Set the window's caption
    pygame.display.set_caption("Space Invaders")

    # Create new game instance and start the game
    game = SpaceGame()
    game.start()


if __name__ == '__main__':
    main()