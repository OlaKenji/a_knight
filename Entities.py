import pygame, sys

class player(pygame.sprite.Sprite):

    images={1: pygame.image.load("sprites/Walk1.png"),#right
            2: pygame.image.load("sprites/Walk2.png"),#right
            3: pygame.transform.flip(pygame.image.load("sprites/Walk1.png"),True,False),#left
            4: pygame.transform.flip(pygame.image.load("sprites/Walk2.png"),True,False)}#left

    images_sword={1: pygame.image.load("sprites/Sword1.png"),#right
                  2: pygame.image.load("sprites/Sword2.png"),#right
                  3: pygame.transform.flip(pygame.image.load("sprites/Sword1.png"),True, False),#left
                  4: pygame.transform.flip(pygame.image.load("sprites/Sword2.png"),True, False),#left
                  5: pygame.image.load("sprites/Sword3.png"),#up-right
                  6: pygame.image.load("sprites/Sword4.png"),#up-right
                  7: pygame.transform.flip(pygame.image.load("sprites/Sword3.png"),True, False),##up-left
                  8: pygame.transform.flip(pygame.image.load("sprites/Sword4.png"),True, False)}##up-left

    velocity=[0,0]
    acceleration=[2,1]
    friction=0.2

    def __init__(self,pos):
        super().__init__()
        self.image = self.images[1]
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        #self.hitbox = self.rect.copy()
        self.movement=[0,0]
        self.dir=[1,0]#[horixontal (right 1, left -1),vertical (up 1, down -1)]
        self.alive=True
        self.frame={'stand':1,'run':1,'sword':1}
        self.action={'stand':True,'run':False,'sword':False,'jump':True}
        self.frame_timer={'run':10,'sword':10,'jump':10}

    def move(self):#define the movements
        self.frame_timer['jump']+=1#air timer

        #game input
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.action['run']=True
                    self.action['stand']=False
                    self.dir[0]=1
                if event.key == pygame.K_LEFT:
                    self.action['run']=True
                    self.action['stand']=False
                    self.dir[0]=-1
                if event.key == pygame.K_UP:#press up
                    self.dir[1]=1
                if event.key == pygame.K_DOWN:#press down
                    self.dir[1]=-1
                if event.key==pygame.K_SPACE and self.frame_timer['jump']<10:#jump
                    self.movement[1]=-10
                    self.action['jump']=True
                if event.key==pygame.K_f:
                    self.action['sword']=True

            elif event.type == pygame.KEYUP:#lift bottom
                if event.key == pygame.K_RIGHT:
                    self.action['stand']=True
                    self.action['run']=False
                if event.key == pygame.K_LEFT:
                    self.action['stand']=True
                    self.action['run']=False
                if event.key == pygame.K_UP:
                    self.dir[1]=0
                if event.key == pygame.K_DOWN:
                    self.dir[1]=0

    def update(self,pos):
        self.rect.topleft = [self.rect.topleft[0] + pos[0], self.rect.topleft[1] + pos[1]]

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

class Items():

    def __init__(self,entity):
        super().__init__()

        self.movement=[0,0]
        self.rect=pygame.Rect(entity.rect.midright[0],entity.rect.midright[1],10,15)

    def update(self,entity):
        if entity.dir[0]>0:#right
            self.rect=pygame.Rect(entity.rect.midright[0],entity.rect.midright[1]-5,10,15)
        elif entity.dir[0]<0:#left
            self.rect=pygame.Rect(entity.rect.midleft[0]-10,entity.rect.midleft[1]-5,10,15)
        elif entity.dir[1]>0:#up
            self.rect=pygame.Rect(entity.rect.midtop[0],entity.rect.midtop[1],10,20)


#class Sword(Items):
#    def __init__(self,entity):
#        super().__init__()
#        self.rect.center = entity.rect.midright
