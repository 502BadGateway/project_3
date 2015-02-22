"""

This file is a stand alone testing script
It will run the same sorting animation as the final project will
However, we are over a week away from completion.
This, when completed will allow the group to test their own sorting algorithms

"""

import pygame

pygame.init()

class display:

	def __init__(self):


		self.displaySort = pygame.display.set_mode((1280, 720))
		self.background = pygame.image.load(sortBackground)
		self.size = self.background.get_size()

	def updateRobot(self):

		self.display.blit(sortBot.image, (sortBot.rect.x, sortBot.rect.y)) #Blits robot image to screen




class sortBot:

	def __init__(self, Sprite):
		pygame.sprite.Sprite.__init__(self, Sprite)
		if sortBot.image is None:             #Loads image dispite some sort of pygame feature to do with Sprites.
			sortBot.image = pygame.image.load("robot.png")

		self.image = sortBot.image
		self.name = ""
		self.points = ""
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 0
		self.targetX = 0
		self.targetY = 0

	def returnRectX(self):
		return self.rect.x

	def returnRectY(self):
		return self.rect.y


barry = sortBot(pygame.sprite.Sprite)
barry.name = "Barry"
barry.points = 0
self.rect.x = 100
self.rect.y = 100

"""

 #For Later

	def moveToTarget(self):

		if(self.rect.x > self.targetX): #If robot is currently 
			self.rect.x = self.rect.x - 1 

"""
