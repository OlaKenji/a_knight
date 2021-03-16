import pygame
import Engine
import Entities
import Level
import Action

pygame.init()#initilise
screen=pygame.display.set_mode((800,600))
clock=pygame.time.Clock()

platforms = pygame.sprite.Group()
hero = pygame.sprite.Group()

knight=Entities.player([400,300])
hero.add(knight)

map=Level.Tilemap()
map.define_chunks('./Tiled/Level1.csv')
platforms.add(map.load_tiles())#whole map

def draw():
    platforms.draw(screen)
    hero.draw(screen)

def scrolling():
    map.true_scroll[0]+=(knight.rect.center[0]-map.true_scroll[0]-410)
    map.true_scroll[1]+=(knight.rect.center[1]-map.true_scroll[1]-328)

    map.scroll=map.true_scroll.copy()
    map.scroll[0]=int(map.scroll[0])
    map.scroll[1]=int(map.scroll[1])

    platforms.update([-map.scroll[0],-map.scroll[1]])
    hero.update([-map.scroll[0],-map.scroll[1]])

while True:
    screen.fill((255,255,255))#fill screen

    #platforms=map.load_chunks()

    scrolling()

    knight.move()

    Engine.Physics.movement(hero)
    Engine.Collisions.check_collisions(hero,platforms)

    Engine.Animation.set_img(hero)

    Action.swing_sword(hero,platforms)

    pygame.draw.rect(screen, (255,0,0), knight.rect,2)#checking hitbox
    pygame.draw.rect(screen, (0,255,0), knight.hitbox,2)#checking hitbox

    draw()
    pygame.display.update()#update after every change
    clock.tick(60)#limmit FPS
