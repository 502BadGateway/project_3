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
class sortBot(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.name = ""
		self.points = 0
		self.targetX = 0
		self.targetY = 0
		self.dir = 0
		self.image = pygame.image.load('ASSETS/car.png')
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 0

	def update(self):
		oldCenter = self.rect.center
		self.image = pygame.transform.rotate(self.image, self.dir)
		self.rect = self.image.get_rect()
		self.rect.center = oldCenter
		screen.blit(self.image, (self.rect.x, self.rect.y))

	def turnLeft(self):
		self.dir = 90
		print "LEFT"
    
	def turnRight(self):
		self.dir = -90
		print "RIGHT"




theSortBot = sortBot()
theSortBot.name = "Fred"
theSortBot.rect.x = 150
theSortBot.rect.y = 500
theSortBot.dir = 0

treasureList = []
x = 0
allSprites = pygame.sprite.Group(theSortBot) #Adds all the sprites into a group saving me updating 8 objects

while 1:
	for event in pygame.event.get(): #Quit sequence
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	allSprites.update() #Ensures screen updates

	allSprites.clear(screen, background) #Cleans up sprutes

	theSortBot.turnLeft()

	allSprites.draw(screen) #Clears the sprites aswell (no idea why i need both, but i do)

	pygame.display.update() #updates everything

	time.sleep(1)




