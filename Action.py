import pygame
import Entities

def swing_sword(sword_enteties,targets):
    for entity in sword_enteties.sprites():#go through the group

        if entity.action['sword']:#if swinning sword
            sword=Entities.Items(entity)#make a sword hitbox

            #collisions=pygame.sprite.groupcollide(swords,entities,True,False)#flag to remove sword entity

            #update sword position based on swing direction
            sword.update(entity)

            #sword collision?
            collisions=pygame.sprite.spritecollideany(sword,targets)

            if collisions:#if sword hit

                if entity.dir[1]>0:#up
                    entity.movement[1]=1#knock back
                elif entity.dir[1]<0:#down
                    entity.movement[1]=-5#knock back
                elif entity.dir[0]>0:#right
                    entity.velocity[0]=-10
                    #entity.movement[0]=-2#knock back
                elif entity.dir[0]<0:#left
                    entity.velocity[0]=10#knock back
