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
		self.location = 0
		self.dir = 0 #direction turning
		self.image = pygame.image.load('ASSETS/car.png') #loads image
		self.rect = self.image.get_rect() #gets the rect
		self.rect.x = 0 #stores coord x
		self.rect.y = 0 #stores coord y
		self.carrying = ""

	def turnLeft(self): #charges turning var to left 
		self.dir = 90 #Makes dir left turning
		oldCenter = self.rect.center #Stores the old centre here
 		self.image = pygame.transform.rotate(self.image, self.dir) #turns car
		self.rect = self.image.get_rect() #gets the rect
		self.rect.center = oldCenter #returns the old centre
		screen.blit(self.image, (self.rect.x, self.rect.y)) #blit it on screen
    
	def turnRight(self): #changes turning var to right 
		self.dir = -90 #makes dir right turning
		oldCenter = self.rect.center #sotrs old centre
		self.image = pygame.transform.rotate(self.image, self.dir) #rotates the robot
		self.rect = self.image.get_rect() #gets the rect
		self.rect.center = oldCenter #returns the old centre
		screen.blit(self.image, (self.rect.x, self.rect.y)) #blit it on screen

	def update(self):
		screen.blit(self.image, (self.rect.x, self.rect.y)) #updates image on screen

class treasure(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.name = ""
		self.image = pygame.image.load('ASSETS/testTreasure.png')
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 0
		self.points = 0
		self.location = 0

	def update(self):
		screen.blit(self.image, (self.rect.x, self.rect.y))

treasure1 = treasure()
treasure1.location = 5
treasure1.rect.x = ((treasure1.location * 142) + 150)
treasure1.rect.y = 280



theSortBot = sortBot()
theSortBot.name = "Fred"
theSortBot.rect.x = ((1 * 142) + 150) 
"""
The one above, is a place holder for the treasure variable.
I NEED THIS DONT TOUCH
"""
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

	theSortBot.update()
	treasure1.update()

	pygame.display.update() #updates everything

	time.sleep(1)




