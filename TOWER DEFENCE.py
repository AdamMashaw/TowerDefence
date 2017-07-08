import pygame
from math import *
from random import *


Black = (0,0,0)
White = (255,255,255)

pygame.init()
Display = [800,600]
gameDisplay = pygame.display.set_mode((Display[0],Display[1]))
pygame.display.set_caption('Family Issues')
clock = pygame.time.Clock()

Player1 = pygame.image.load('Char1.png')
Player2 = pygame.image.load('Char2.png')
x = (Display[0] * .45)
y = (Display[1] * .8)


def Player(Player,x,y):
   if Player == 0:
      gameDisplay.blit(Player1,(x,y))
   if Player == 1:
      gameDisplay.blit(Player2,(x,y))
   return

def hit(Player,x,y,x2,y2):
   has_hit = True
   

   return has_hit


def Strike(Player,x,y,x2,y2):
   Damage = 0
   if Player == 0:
      if hit(0,x,y,x2,y2) == True:
         Damage = randint(10,13)
   if Player == 1:
      if hit(1,x,y,x2,y2) == True:
         Damage = randint(10,13)
   return Damage
   

   return
posx = (Display[0] * .45)
y = (Display[1] * .8)

def Game_Run():

   x1 = (Display[0] * .45)
   y1 = (Display[1] * .8)

   x2 = (Display[0] * .6)
   y2 = (Display[1] * .8)

   game_Exit = False

   ChangeX1 = 0
   ChangeY1 = 0

   ChangeX2 = 0
   ChangeY2 = 0
   
   Pos1 = 0
   Pos2 = 0
   
   while not game_Exit:
      
      Damage = 0
      Damage1 = 0
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            game_Exit = True

         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
               ChangeX1 = -2
               Pos1 = 1
            if event.key == pygame.K_d:
               ChangeX1 = 2
               Pos1 = 3
            if event.key == pygame.K_w:
               ChangeY1 = -2
               Pos1 = 2
            if event.key == pygame.K_s:
               ChangeY1 = 2
               Pos1 = 0
            if event.key == pygame.K_e:
               Damage = Strike(0,x1,y1,0,0)
               print("Player 1 D:", Damage)
               
            if event.key == pygame.K_LEFT:
               ChangeX2 = -2
               Pos2 = 1
            if event.key == pygame.K_RIGHT:
               ChangeX2 = 2
               Pos2 = 3
            if event.key == pygame.K_UP:
               ChangeY2 = -2
               Pos2 = 2
            if event.key == pygame.K_DOWN:
               ChangeY2 = 2
               Pos2 = 0
            if event.key == pygame.K_RCTRL:
               Damage1 = Strike(1,x2,y2,0,0)
               print("Player 2 D:", Damage1)
               
         if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
               ChangeY1 = 0
            if event.key == pygame.K_s:
               ChangeY1 = 0
            if event.key == pygame.K_a:
               ChangeX1 = 0
            if event.key == pygame.K_d:
               ChangeX1 = 0

            if event.key == pygame.K_UP:
               ChangeY2 = 0
            if event.key == pygame.K_DOWN:
               ChangeY2 = 0
            if event.key == pygame.K_LEFT:
               ChangeX2 = 0
            if event.key == pygame.K_RIGHT:
               ChangeX2 = 0

               
      x1 = x1 + ChangeX1
      y1 = y1 + ChangeY1

      x2 += ChangeX2
      y2 += ChangeY2
      
      gameDisplay.fill(White)
      Player(0,x1,y1)
      Player(1,x2,y2)
      pygame.display.update()
      clock.tick(60)
      
   pygame.quit()
   quit()
Game_Run()
