import pygame
import sys

class treasurePos(mapSelected):
	def mapTreasurePos(self,mapSelected):
		pygame.init()

		#create display
		self.size = width, height = 1280, 1280
		self.display = pygame.display.set_mode(self.size)
		self.background = pygame.image.load(mapSelected)
		self.display.blit(self.background,(0,0))

		i = 0
		while i < 5:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

				elif event.type == pygame.MOUSEBUTTONDOWN:
					x, y = event.pos
					treasurePosListX[i] = x
					treasurePosListY[i] = y
					i=i+1