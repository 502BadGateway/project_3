"""

This file is a stand alone testing script
It will run the same sorting animation as the final project will
However, we are over a week away from completion.
This, when completed will allow the group to test their own sorting algorithms

"""
import sys
import pygame
from pygame.locals import *
import time

pygame.init()

screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Sort Bot")
background = pygame.image.load('ASSETS/sortBackground.png')
screen.blit(background, (0,0))
class sortBot(pygame.sprite.Sprite): #calls sprite base class

	def __init__(self):
		pygame.sprite.Sprite.__init__(self) #initialised base class
		self.name = "" #gives robot a name
		self.points = 0 #gives robot points
		self.targetX = 0 #robots target x
		self.targetY = 0 #robots target y
		self.dir = 0 #direction turning
		self.image = pygame.image.load('ASSETS/car.png') #loads image
		self.rect = self.image.get_rect() #gets the rect
		self.rect.x = 0 #stores coord x
		self.rect.y = 0 #stores coord y

	def update(self): #updates robot when turning
		oldCenter = self.rect.center
		self.image = pygame.transform.rotate(self.image, self.dir)
		self.rect = self.image.get_rect()
		self.rect.center = oldCenter
		screen.blit(self.image, (self.rect.x, self.rect.y))

	def turnLeft(self): #charges turning var to left 
		self.dir = 90
    
	def turnRight(self): #changes turning var to right 
		self.dir = -90




theSortBot = sortBot()
theSortBot.name = "Fred"
theSortBot.rect.x = 150
theSortBot.rect.y = 500
theSortBot.dir = 0

treasureList = []
x = 0

while 1:
	for event in pygame.event.get(): #Quit sequence
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	screen.blit(background, (0,0))
	theSortBot.update() #Ensures screen updates

	theSortBot.turnLeft() #turns sortBot

	pygame.display.update() #updates everything

	time.sleep(1)




