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


class sortBot:

	def __init__(self):
	pygame.sprite.Sprite.__init__(self)
			if sortBot.image is none:             #Loads image dispite some sort of pygame feature to do with Sprites.
				sortBot.image = pygame.image.load("robot.png")

	self.image = sortBot.image
	self.name = ""
	self.points = ""
	self.rect = self.image.get_rect()
	self.rect.x = 0
	self.rect.y = 0

	def returnRectX():
		return self.rect.x

	def returnRectY():
		return self.rect.y

