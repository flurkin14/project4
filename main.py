import pygame, sys, time, random

pygame.init()
win=pygame.display.set_mode((500, 500))
speed=5

yellow=(255, 255, 0)
white=(255, 255, 255)
red=(255, 0, 0)
green=(0, 255, 0)
playerx=250
playery=250

while(True):
  pygame.time.delay(10)
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
  keys=pygame.key.get_pressed()
  win.fill(white)
  if(keys[pygame.K_RIGHT]):
    playerx+=speed
  if(keys[pygame.K_LEFT]):
    playerx-=speed
  if(keys[pygame.K_DOWN]):
    playery+=speed
  if(keys[pygame.K_UP]):
    playery-=speed


  

  player=pygame.Rect(playerx, playery, 30,30)
  pygame.draw.rect(win, red, player)
  food=pygame.Rect(400,250,10,10)
  pygame.draw.rect(win, green, food)
  pygame.display.update()


  if player.colliderect(food):
    print("you are eating")
