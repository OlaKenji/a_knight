import pygame, sys

class player(pygame.sprite.Sprite):

    images={1: pygame.image.load("sprites/Walk1.png"),
            2: pygame.image.load("sprites/Walk2.png"),
            3: pygame.image.load("sprites/Sword1.png"),
            4: pygame.image.load("sprites/Sword2.png")}

    velocity=[2,1]

    def __init__(self,pos):
        super().__init__()
        self.frame=1
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        #self.hitbox = self.rect.copy()
        self.movement=[0,1]
        self.alive=True
        self.air_timer=10
        self.action='stand'
        self.sword_timer=10

    def move(self):#define the movements
        self.movement[1]+=1#gravity
        self.air_timer+=1#air timer

        if self.movement[1]>5:#set a y max speed
            self.movement[1]=5

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.movement[0]=self.velocity[0]
                    self.action='run'
                if event.key == pygame.K_LEFT:
                    self.movement[0]=-self.velocity[0]
                    self.action='run'
                if event.key==pygame.K_SPACE and self.air_timer<10:#jump
                    self.movement[1]=-10
                    self.action='jump'
                if event.key==pygame.K_f:
                    self.action='sword'
                    self.sword_timer=0
                    self.frame=0

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT and self.movement[0]>0:
                    self.movement[0]=0
                    self.action='stand'
                if event.key == pygame.K_LEFT and self.movement[0]<0:
                    self.movement[0]=0
                    self.action='stand'
                if event.key==pygame.K_f:
                    self.action='stand'

    def update(self,pos):
        self.rect.topleft = [self.rect.topleft[0] + pos[0], self.rect.topleft[1] + pos[1]]
        self.set_image()#update the image
        self.sword_timer+=1

    def set_image(self):
        if self.action=='run' and self.sword_timer>2:
            self.frame+=1
            if self.frame>59:
                self.frame=1
            self.image = self.images[self.frame//30+1]
        elif self.action=='sword':
            self.frame+=1
            if self.frame>2:
                self.frame=1
            self.image = self.images[self.frame//2+3]
        elif self.action=='stand' and self.sword_timer>2:
            self.frame=1
            self.image = self.images[self.frame]

class Block(pygame.sprite.Sprite):

    images = {1 : pygame.image.load("sprites/block_castle.png"),
             2 : pygame.image.load("sprites/block_question.png")}

    def __init__(self,img,pos,chunk_key):
        super().__init__()
        self.image = self.images[img]
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        #self.hitbox = self.rect.inflate(0,0)
        self.chunk_key=chunk_key

    def update(self,pos):
        self.rect.topleft = [self.rect.topleft[0] + pos[0], self.rect.topleft[1] + pos[1]]
        #self.hitbox = self.rect.inflate(0,0)
