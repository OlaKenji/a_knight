import pygame
import Engine
import Entities
import Level

pygame.init()#initilise
screen=pygame.display.set_mode((800,600))
clock=pygame.time.Clock()

platforms = pygame.sprite.Group()
hero = pygame.sprite.Group()

link=Entities.player([400,300])
hero.add(link)

map=Level.Tilemap()
map.divide_chunks('./Tiled/Level1.csv')

#platforms.add(map.load_tiles())#whole map

def draw():
    platforms.draw(screen)
    hero.draw(screen)

def scrolling():
    map.scroll[0]+=(-link.rect.center[0]-map.scroll[0]+400)
    map.scroll[1]+=(-link.rect.center[1]-map.scroll[1]+300)

    map.scroll[0]=round(map.scroll[0])
    map.scroll[1]=round(map.scroll[1])

    hero.update(map.scroll)
    platforms.update(map.scroll)

while True:
    screen.fill((255,255,255))#fill screen

    platforms=map.load_chunks()

    scrolling()

    link.move()
    Engine.check_collisions(hero,platforms,'Player')
    print('hej')
    draw()
    pygame.display.update()#update after every change
    clock.tick(60)#limmit FPS
