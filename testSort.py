"""

This file is a stand alone testing script
It will run the same sorting animation as the final project will
However, we are over a week away from completion.
This, when completed will allow the group to test their own sorting algorithms

"""



import pygame

class display:

	def __init__(self):

		self.displaySort = pygame.display.set_mode((1280, 720))
		self.background = pygame.image.load(sortBackground)