import pygame, sys

class player(pygame.sprite.Sprite):

    images={1: pygame.image.load("sprites/HeroKnight_Run_0.png"),#right
            2: pygame.image.load("sprites/HeroKnight_Run_1.png"),#right
            3: pygame.image.load("sprites/HeroKnight_Run_2.png"),#right
            4: pygame.image.load("sprites/HeroKnight_Run_3.png"),#right
            5: pygame.image.load("sprites/HeroKnight_Run_4.png"),#right
            6: pygame.image.load("sprites/HeroKnight_Run_5.png"),#right
            7: pygame.image.load("sprites/HeroKnight_Run_6.png"),#right
            8: pygame.image.load("sprites/HeroKnight_Run_7.png"),#right
            9: pygame.image.load("sprites/HeroKnight_Run_8.png"),#right
            10: pygame.image.load("sprites/HeroKnight_Run_9.png"),#right
            11: pygame.transform.flip(pygame.image.load("sprites/HeroKnight_Run_0.png"),True,False),#left
            12: pygame.transform.flip(pygame.image.load("sprites/HeroKnight_Run_1.png"),True,False),#left
            13: pygame.transform.flip(pygame.image.load("sprites/HeroKnight_Run_2.png"),True,False),#left
            14: pygame.transform.flip(pygame.image.load("sprites/HeroKnight_Run_3.png"),True,False),#left
            15: pygame.transform.flip(pygame.image.load("sprites/HeroKnight_Run_4.png"),True,False),#left
            16: pygame.transform.flip(pygame.image.load("sprites/HeroKnight_Run_5.png"),True,False),#left
            17: pygame.transform.flip(pygame.image.load("sprites/HeroKnight_Run_6.png"),True,False),#left
            18: pygame.transform.flip(pygame.image.load("sprites/HeroKnight_Run_7.png"),True,False),#left
            19: pygame.transform.flip(pygame.image.load("sprites/HeroKnight_Run_8.png"),True,False),#left
            20: pygame.transform.flip(pygame.image.load("sprites/HeroKnight_Run_9.png"),True,False),#left
            21: pygame.image.load("sprites/HeroKnight_Jump_0.png"),#jumpright
            22: pygame.image.load("sprites/HeroKnight_Jump_1.png"),#jumpright
            23: pygame.image.load("sprites/HeroKnight_Jump_2.png"),#jumpright
            24: pygame.transform.flip(pygame.image.load("sprites/HeroKnight_Jump_0.png"),True,False),#jumpleft
            25: pygame.transform.flip(pygame.image.load("sprites/HeroKnight_Jump_1.png"),True,False),#jumpleft
            26: pygame.transform.flip(pygame.image.load("sprites/HeroKnight_Jump_2.png"),True,False)}#jumpleft

    images_sword={1: pygame.image.load("sprites/HeroKnight_Attack3_0.png"),#right
                  2: pygame.image.load("sprites/HeroKnight_Attack3_1.png"),#right
                  3: pygame.image.load("sprites/HeroKnight_Attack3_2.png"),#right
                  4: pygame.image.load("sprites/HeroKnight_Attack3_3.png"),#right
                  5: pygame.image.load("sprites/HeroKnight_Attack3_4.png"),#right
                  6: pygame.image.load("sprites/HeroKnight_Attack3_5.png"),#right
                  7: pygame.transform.flip(pygame.image.load("sprites/HeroKnight_Attack3_0.png"),True, False),#left
                  8: pygame.transform.flip(pygame.image.load("sprites/HeroKnight_Attack3_1.png"),True, False),#left
                  9: pygame.transform.flip(pygame.image.load("sprites/HeroKnight_Attack3_2.png"),True, False),#left
                  10: pygame.transform.flip(pygame.image.load("sprites/HeroKnight_Attack3_3.png"),True, False),#left
                  11: pygame.transform.flip(pygame.image.load("sprites/HeroKnight_Attack3_4.png"),True, False),#left
                  12: pygame.transform.flip(pygame.image.load("sprites/HeroKnight_Attack3_5.png"),True, False),#left
                  13: pygame.image.load("sprites/HeroKnight_Attack1_0.png"),#upright
                  14: pygame.image.load("sprites/HeroKnight_Attack1_1.png"),#upright
                  15: pygame.image.load("sprites/HeroKnight_Attack1_2.png"),#upright
                  16: pygame.image.load("sprites/HeroKnight_Attack1_3.png"),#upright
                  17: pygame.image.load("sprites/HeroKnight_Attack1_4.png"),#upright
                  18: pygame.image.load("sprites/HeroKnight_Attack1_5.png"),#upright
                  19: pygame.transform.flip(pygame.image.load("sprites/HeroKnight_Attack1_0.png"),True, False),#upleft
                  20: pygame.transform.flip(pygame.image.load("sprites/HeroKnight_Attack1_1.png"),True, False),#upleft
                  21: pygame.transform.flip(pygame.image.load("sprites/HeroKnight_Attack1_2.png"),True, False),#upleft
                  22: pygame.transform.flip(pygame.image.load("sprites/HeroKnight_Attack1_3.png"),True, False),#upleft
                  23: pygame.transform.flip(pygame.image.load("sprites/HeroKnight_Attack1_4.png"),True, False),#upleft
                  24: pygame.transform.flip(pygame.image.load("sprites/HeroKnight_Attack1_5.png"),True, False),#upleft
                  25: pygame.transform.flip(pygame.image.load("sprites/HeroKnight_Attack2_0.png"),True, False),#down
                  26: pygame.transform.flip(pygame.image.load("sprites/HeroKnight_Attack2_1.png"),True, False),#down
                  27: pygame.transform.flip(pygame.image.load("sprites/HeroKnight_Attack2_2.png"),True, False),#down
                  28: pygame.transform.flip(pygame.image.load("sprites/HeroKnight_Attack2_3.png"),True, False),#down
                  29: pygame.transform.flip(pygame.image.load("sprites/HeroKnight_Attack2_4.png"),True, False),#down
                  30: pygame.transform.flip(pygame.image.load("sprites/HeroKnight_Attack2_5.png"),True, False)}#down


    velocity=[0,0]
    acceleration=[2,1]
    friction=0.2

    def __init__(self,pos):
        super().__init__()
        self.image = self.images[1]
        self.rect = self.image.get_rect(center=pos)
        self.hitbox=pygame.Rect(pos[0],pos[1],20,48)
        self.rect.center=self.hitbox.center#match the hitboxes

        self.movement=[0,0]
        self.dir=[1,0]#[horixontal (right 1, left -1),vertical (up 1, down -1)]
        self.alive=True
        self.frame={'stand':1,'run':1,'sword':1,'jump':1}
        self.action={'stand':True,'run':False,'sword':False,'jump':False}
        self.frame_timer={'run':40,'sword':18,'jump':21}


    def move(self):#define the movements

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
                if event.key==pygame.K_SPACE and self.action['jump']==False:#jump
                    self.movement[1]=-10
                    self.action['jump']=True
                if event.key==pygame.K_f:
                    self.action['sword']=True

            elif event.type == pygame.KEYUP:#lift bottom
                if event.key == pygame.K_RIGHT and self.dir[0]>0:
                    self.action['stand']=True
                    self.action['run']=False
                if event.key == pygame.K_LEFT and self.dir[0]<0:
                    self.action['stand']=True
                    self.action['run']=False
                if event.key == pygame.K_UP:
                    self.dir[1]=0
                if event.key == pygame.K_DOWN:
                    self.dir[1]=0

    def update(self,pos):
        self.rect.topleft = [self.rect.topleft[0] + pos[0], self.rect.topleft[1] + pos[1]]
        self.hitbox.center=self.rect.center

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
        self.rect=pygame.Rect(entity.hitbox.midright[0],entity.hitbox.midright[1],10,15)

    def update(self,entity):
        if entity.dir[0]>0 and entity.dir[1]==0:#right
            self.rect=pygame.Rect(entity.hitbox.midright[0],entity.hitbox.midright[1],10,20)
        elif entity.dir[0]<0 and entity.dir[1]==0:#left
            self.rect=pygame.Rect(entity.hitbox.midleft[0]-10,entity.hitbox.midleft[1],10,20)
        elif entity.dir[1]>0:#up
            self.rect=pygame.Rect(entity.hitbox.midtop[0],entity.hitbox.midtop[1]-50,10,20)
        elif entity.dir[1]<0:#down
            self.rect=pygame.Rect(entity.hitbox.midtop[0],entity.hitbox.midtop[1]+50,10,20)
            
#class Sword(Items):
#    def __init__(self,entity):
#        super().__init__()
#        self.rect.center = entity.rect.midright
