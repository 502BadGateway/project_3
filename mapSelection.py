import pygame
import sys


class mapSelect():
	def mapPanel(self):
		pygame.init()

		#create display
		self.size = width, height = 510, 320
		self.display = pygame.display.set_mode(self.size)
		background = pygame.Surface(self.display.get_size())
		background = background.convert()
		background.fill((250, 250, 250))
		self.display.blit(background,(0,0))
		#pygame.display.set_catption("Map Selection")

		#load in button images
		self.London = pygame.image.load("London.png")
		self.Paris = pygame.image.load("Paris.png")
		self.NewYork = pygame.image.load("New York.png")
		self.Tokyo = pygame.image.load("Tokyo 2.png")
		self.Johnasabergg = pygame.image.load("Johnasabergg.png")
		self.Berlin = pygame.image.load("Berlin.png")

		#make all the images the same size
		self.London = pygame.transform.scale(self.London,(130,100))
		self.Paris = pygame.transform.scale(self.Paris,(130,100))
		self.NewYork = pygame.transform.scale(self.NewYork,(130,100))
		self.Tokyo = pygame.transform.scale(self.Tokyo,(130,100))
		self.Johnasabergg = pygame.transform.scale(self.Johnasabergg,(130,100))
		self.Berlin = pygame.transform.scale(self.Berlin,(130,100))

		#butttons
		L = self.display.blit(self.London,(30,40))
		P = self.display.blit(self.Paris,(190,40))
		N = self.display.blit(self.NewYork,(350,40))
		T = self.display.blit(self.Tokyo, (30,180))
		J = self.display.blit(self.Johnasabergg, (190,180))
		B = self.display.blit(self.Berlin, (350,180))

		pygame.display.flip()

		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

				elif event.type == pygame.MOUSEBUTTONDOWN:
					x, y = event.pos
					print "click",x,y
					
map1 = mapSelect()
map1.mapPanel()


