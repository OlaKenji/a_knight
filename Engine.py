import pygame

#collisions between enteties-groups: a dynamic and a static one
def collision(dynamic_entties,static_enteties):
    collision_types = {'top':False,'bottom':False,'right':False,'left':False}

    #move in x every dynamic sprite
    for entity in dynamic_entties.sprites():
        entity.rect.topleft = [entity.rect.topleft[0] + entity.movement[0], entity.rect.topleft[1] + 0]

    #check for collisions and get a dictionary of sprites that collides
    collisions=pygame.sprite.groupcollide(dynamic_entties,static_enteties,False,False)
    for dyn_entity, stat_entity in collisions.items():
        if dyn_entity.movement[0]>0:#going to the right
            dyn_entity.rect.right = stat_entity[0].rect.left
            collision_types['right'] = True

        elif dyn_entity.movement[0]<0:#going to the left
            dyn_entity.rect.left = stat_entity[0].rect.right
            collision_types['left'] = True

    #move in y every dynamic sprite
    for entity in dynamic_entties.sprites():
        entity.rect.topleft = [entity.rect.topleft[0] + 0, entity.rect.topleft[1] + entity.movement[1]]

    collisions=pygame.sprite.groupcollide(dynamic_entties,static_enteties,False,False)
    for dyn_entity, stat_entity in collisions.items():
        if dyn_entity.movement[1]>0:#going down
            dyn_entity.rect.bottom = stat_entity[-1].rect.top
            collision_types['bottom'] = True

        elif dyn_entity.movement[1]<0:#going up
            dyn_entity.rect.top = stat_entity[-1].rect.bottom
            collision_types['top'] = True

    return collision_types


def check_collisions(hero,platforms,entities):
    collision_types=collision(hero,platforms)

    if entities=='Player':
        for entity in hero.sprites():
            if collision_types['bottom']:
                entity.air_timer=0
            elif collision_types['top']:#knock back when hit head
                entity.movement[1]=1
