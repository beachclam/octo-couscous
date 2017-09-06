#!/bin/python
import sys, pygame, pygame.mixer
from pygame.locals import *
from random import randint

pygame.init()

size=width, height=1600,900
screen = pygame.display.set_mode(size,pygame.RESIZABLE)

clock = pygame.time.Clock()

bullets=[]

background = pygame.image.load("earthmap_hires.jpg")
ship = pygame.image.load("f2.png")
ship = pygame.transform.scale(ship,(64,64))
background_scaled = pygame.transform.scale(background,(1600,900))
bulletpicture = pygame.image.load("f2.png")
f2 = pygame.transform.scale(bulletpicture,(64,64)) 
shot = pygame.mixer.Sound("thud.wav")
soundin = pygame.mixer.Sound("hititson.ogg")
soundin.set_volume(0.1)
soundin.play()

poses = [(10,20), (20, 40), (40, 80), (160, 320)]

'''def circ(x2, y2, r):
    x=r
    y=0
    err=0
    while (x >= y):
        screen.blit(f2, (x2 + x, y0 + y))
        screen.blit(f2, (x2 + y, y0 + x))
        screen.blit(f2, (x2 - y, y0 + x))
        screen.blit(f2, (x2 - x, y0 + y))
        screen.blit(f2, (x2 - x, y0 - y))
        screen.blit(f2, (x2 - y, y0 - x))
        screen.blit(f2, (x2 + y, y0 - x))
        screen.blit(f2, (x2 + x, y0 - y))
        if (err <= 0):
            y+=1
            err+=2*y+1
        if (err > 0):
            x-=1
            err-=2*x+1'''
x2=800
y2=450
r=100
x=r
y=0
err=0
testrotate=0
testrotate2=0

def ori(rotatevalue, randposneg):
    x=randposneg
    y=rotatevalue
    if (x > 4):
        y+=1
        return y
    elif(x < 4):
        y-=1
        return y
    else:
        y+=5
        return y

while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    elif event.type == MOUSEBUTTONDOWN:
      shot.play()
      bullets.append([event.pos[0], 500])
  clock.tick(60)
  mx,my = pygame.mouse.get_pos()
  for b in range(len(bullets)):
    bullets[b][0]-=10
  for bullet in bullets:
    if bullet[0]<0:
      bullets.remove(bullet)
  screen.blit(background_scaled,(0,0))
  for bullet in bullets:
    screen.blit(f2, pygame.Rect(bullet[0], bullet[1], 0, 0))
  screen.blit(ship, (mx, 500))
  screen.blit(pygame.transform.rotate(f2, testrotate), (x2 + x, y2 + y))
  screen.blit(pygame.transform.rotate(f2, testrotate), (x2 + y, y2 + x))
  screen.blit(pygame.transform.rotate(f2, testrotate), (x2 - y, y2 + x))
  screen.blit(pygame.transform.rotate(f2, testrotate), (x2 - x, y2 + y))
  screen.blit(pygame.transform.rotate(f2, testrotate2), (x2 - x, y2 - y))
  screen.blit(pygame.transform.rotate(f2, testrotate2), (x2 - y, y2 - x))
  screen.blit(pygame.transform.rotate(f2, testrotate2), (x2 + y, y2 - x))
  screen.blit(pygame.transform.rotate(f2, testrotate2), (x2 + x, y2 - y))
  if (err <= 0):
     y+=1
     err+=2*y+1
  if (err > 0):
     x-=1
     err-=2*x+1
  pygame.display.update()

