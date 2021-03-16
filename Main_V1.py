import pygame
import Engine
import Entities
import Level
import Action

pygame.init()#initilise
screen=pygame.display.set_mode((800,600))
clock=pygame.time.Clock()


game_font=pygame.font.Font('freesansbold.ttf',25)

platforms = pygame.sprite.Group()
hero = pygame.sprite.Group()

knight=Entities.player([400,300])
hero.add(knight)

map=Level.Tilemap()
map.define_chunks('./Tiled/Level1.csv')
#platforms.add(map.load_tiles())#whole map

def draw():
    platforms.draw(screen)
    hero.draw(screen)

def scrolling():
    map.scroll[0]+=(-knight.rect.center[0]-map.scroll[0]+400)
    map.scroll[1]+=(-knight.rect.center[1]-map.scroll[1]+300)

    map.scroll[0]=round(map.scroll[0])
    map.scroll[1]=round(map.scroll[1])

    hero.update(map.scroll)
    platforms.update(map.scroll)

while True:
    screen.fill((255,255,255))#fill screen

    platforms=map.load_chunks()

    scrolling()

    knight.move()

    Engine.Collisions.check_collisions(hero,platforms)
    Engine.Animation.set_img(hero)
    Engine.Physics.movement(hero)

    Action.swing_sword(hero,platforms)

    pygame.draw.rect(screen, (255,0,0), knight.rect,2)#testing hitbox
    pygame.draw.rect(screen, (0,255,0), knight.hitbox,2)#testing hitbox

    draw()
    pygame.display.update()#update after every change
    clock.tick(60)#limmit FPS
