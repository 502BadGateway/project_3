"""

This file is a stand alone testing script
It will run the same sorting animation as the final project will
However, we are over a week away from completion.
This, when completed will allow the group to test their own sorting algorithms

"""
"""
THE MODULES
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

"""
THE CLASSES
"""

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
		self.target = 0

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

	def moveLeft(self):
		for i in range(0,140):
			self.rect.x -= 1
			screen.blit(background, (self.rect.x, self.rect.y))
			self.update()
			pygame.display.update()
			time.sleep(0.01)
		self.location = self.location - 1
		print self.location

	def moveRight(self):
		for i in range(0,140):
			self.rect.x += 1
			screen.blit(background, (self.rect.x, self.rect.y))
			self.update()
			pygame.display.update()
			time.sleep(0.001)
		self.location = self.location - 1
		print self.location

	def moveToTarget(self):
		while self.location != self.target:
			if self.location > self.target:
				self.moveLeft()
			elif self.location < self.target:
				self.moveRight()



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


"""
THE TREASURES 
"""

treasure1 = treasure()
treasure1.location = 5

treasure2 = treasure()
treasure2.location = 3

treasure3 = treasure()
treasure3.location = 1

treasure4 = treasure()
treasure4.location = 2

treasure5 = treasure()
treasure5.location = 0

treasure6 = treasure()
treasure6.location = 6

treasure7 = treasure()
treasure7.location = 4

treasureList = [treasure1, treasure2, treasure3, treasure4, treasure5, treasure6, treasure7]

for i in treasureList:
	i.rect.x = ((i.location * 142) + 150)
	i.rect.y = 280

"""
THE ROBOT 
"""

theSortBot = sortBot()
theSortBot.name = "Fred"
theSortBot.location = 6
theSortBot.rect.x = ((theSortBot.location * 142) + 150) 
theSortBot.rect.y = 500
theSortBot.dir = 0
theSortBot.target = 4

"""
THE MAIN LOOP
"""

screen.blit(background, (0,0))
pygame.display.update() #updates everything

theSortBot.update()
for i in treasureList:
	i.update()

pygame.display.update()
while 1:
	for event in pygame.event.get(): #Quit sequence
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	theSortBot.moveToTarget()
	theSortBot.update()
	pygame.display.update() #updates everything
	time.sleep(0.1)


