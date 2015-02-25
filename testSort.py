"""

This file is a stand alone testing script
It will run the same sorting animation as the final project will
However, we are over a week away from completion.
This, when completed will allow the group to test their own sorting algorithms

"""
import sys
import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Sort Bot")
background = pygame.image.load('ASSETS/sortBackground.png')
screen.blit(background, (0,0))
class sortBot:

	def __init__(self):

		self.name = ""
		self.points = 0
		self.targetX = 0
		self.targetY = 0
		self.image = pygame.image.load('ASSETS/chuckle-1.png')
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 0

	def updateRobot(self):

		self.image = pygame.transform.scale(self.image, (120,200))
		screen.blit(self.image, (self.rect.x, self.rect.y))
		print "BLIT"


theSortBot = sortBot()
theSortBot.name = "Fred"
theSortBot.rect.x = 150
theSortBot.rect.y = 500

treasureList = []


while 1:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	theSortBot.updateRobot()	

	pygame.display.update()		




