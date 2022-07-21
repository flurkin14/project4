import pygame, sys, time, random

pygame.init()
win=pygame.display.set_mode((500, 500))
speed=5
size=30
yellow=(255, 255, 0)
white=(255, 255, 255)
red=(255, 0, 0)
green=(0, 255, 0)
black=(0,0,0)
playerx=250
playery=250

poison=pygame.Rect(250,150,10,10)
poison_status=True

food=pygame.Rect(400,200,10,10)
food_status=True

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

  player=pygame.Rect(playerx, playery, size,size)


  if player.colliderect(food):
    print("you are eating")
    size+=5
    food_status=False


  if player.colliderect(poison):
    print("you are eating")
    size-=5
    poison_status=False
    
  if (food_status==False):
    food=pygame.Rect(random.randint(1,500),random.randint(1,500),10,10)
    #food=True

  if (poison_status==False):
    poison=pygame.Rect(random.randint(1,500),random.randint(1,500),10,10)
    
  pygame.draw.rect(win, black, poison)
    
  pygame.draw.rect(win, red, player)
  pygame.draw.rect(win, green, food)
  pygame.display.update()


  
