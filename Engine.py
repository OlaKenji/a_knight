import pygame

class Collisions():
    def __init__(self):
        pass

    @staticmethod
    def check_collisions(dynamic_entties,platforms):
        collision_types=Collisions.collide(dynamic_entties,platforms)

        for entity in dynamic_entties.sprites():
            if collision_types['bottom']:
                entity.frame_timer['jump']=0
                entity.action['jump']=False
                entity.action['sword']=False
            elif collision_types['top']:#knock back when hit head
                entity.movement[1]=1

    #collisions between enteties-groups: a dynamic and a static one
    @staticmethod
    def collide(dynamic_entties,static_enteties,kill_dyn=False):
        collision_types = {'top':False,'bottom':False,'right':False,'left':False}

        #move in x every dynamic sprite
        for entity in dynamic_entties.sprites():
            entity.rect.center = [round(entity.rect.center[0] + entity.movement[0]), entity.rect.center[1] + 0]

        #check for collisions and get a dictionary of sprites that collides
        collisions=pygame.sprite.groupcollide(dynamic_entties,static_enteties,kill_dyn,False)

        for dyn_entity, stat_entity in collisions.items():
            if dyn_entity.movement[0]>0:#going to the right
                dyn_entity.rect.right = stat_entity[0].rect.left
                collision_types['right'] = True

            elif dyn_entity.movement[0]<0:#going to the left
                dyn_entity.rect.left = stat_entity[0].rect.right
                collision_types['left'] = True

        #move in y every dynamic sprite
        for entity in dynamic_entties.sprites():
            entity.rect.center = [entity.rect.center[0] + 0, entity.rect.center[1] + entity.movement[1]]

        collisions=pygame.sprite.groupcollide(dynamic_entties,static_enteties,kill_dyn,False)
        for dyn_entity, stat_entity in collisions.items():
            if dyn_entity.movement[1]>0:#going down
                dyn_entity.rect.bottom = stat_entity[-1].rect.top
                collision_types['bottom'] = True

            elif dyn_entity.movement[1]<0:#going up
                dyn_entity.rect.top = stat_entity[-1].rect.bottom
                collision_types['top'] = True

        return collision_types

class Physics():
    def __init__(self):
        pass

    @staticmethod
    def movement(dynamic_entties):
        for entity in dynamic_entties.sprites():

            entity.movement[1]+=entity.acceleration[1]#gravity
            if entity.movement[1]>5:#set a y max speed
                entity.movement[1]=5

            if entity.action['run'] and entity.dir[0]>0:#accelerate right
                entity.velocity[0]+=entity.acceleration[0]
                if entity.velocity[0]>10:
                    entity.velocity[0]=10
            elif entity.action['run'] and entity.dir[0]<0:#accelerate left
                entity.velocity[0]+=-entity.acceleration[0]
                if entity.velocity[0]<-10:
                    entity.velocity[0]=-10

            entity.velocity[0]=round(entity.velocity[0]-0.2*entity.velocity[0],2)#friction

            entity.movement[0]=entity.velocity[0]#set the velocity

class Animation():
    def __init__(self):
        #super().__init__()
        pass

    @staticmethod
    def set_img(enteties):
        for entity in enteties.sprites():#go through the group

            #need to order according to priority
            #can maybe generalise this code into a loop

            #sword
            if entity.action['sword']==True and entity.dir[1]>0 and entity.dir[0]>0:#sword up-right
                entity.image=entity.images_sword[entity.frame['sword']//5+5]
                entity.frame['sword']+=1
            elif entity.action['sword']==True and entity.dir[1]>0 and entity.dir[0]<0:#sword up-left
                entity.image=entity.images_sword[entity.frame['sword']//5+7]
                entity.frame['sword']+=1
            elif entity.action['sword']==True and entity.dir[0]>0 and entity.dir[1]==0:#sword right
                entity.image=entity.images_sword[entity.frame['sword']//5+1]
                entity.frame['sword']+=1
            elif entity.action['sword']==True and entity.dir[0]<0 and entity.dir[1]==0:#sword left
                entity.image=entity.images_sword[entity.frame['sword']//5+3]
                entity.frame['sword']+=1
            elif entity.action['sword']==True and entity.action['jump']==True and entity.dir[1]<0:#jump down
                entity.image=entity.images_sword[entity.frame['sword']//5+9]
                entity.frame['sword']+=1

            #jump
            elif entity.action['jump']==True and not entity.action['sword']:#jump down
                entity.image=entity.images[5]
            #run
            elif entity.action['run']==True and entity.dir[0]>0:#run right
                entity.image=entity.images[entity.frame['run']//5+1]
                entity.frame['run']+=1
            elif entity.action['run']==True and entity.dir[0]<0:#run left
                entity.image=entity.images[entity.frame['run']//5+3]
                entity.frame['run']+=1

            #stand
            elif entity.action['stand']==True and entity.dir[0]>0:#stand right
                entity.image=entity.images[1]
            elif entity.action['stand']==True and entity.dir[0]<0:#stand left
                entity.image=entity.images[3]

            #reset frames
            if entity.frame['sword']==entity.frame_timer['sword']:
                entity.frame['sword']=1
                entity.action['sword']=False

            if entity.frame['run']==entity.frame_timer['run']:
                entity.frame['run']=1
