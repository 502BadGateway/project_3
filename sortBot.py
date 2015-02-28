import pygame
from robot import *

class SortBot(robot, pygame.sprite.Sprite): #class called sortbot.

	def __init__(self, treasureList): #initialises sortbot
		pygame.sprite.Sprite.__init__(self) #initalises sprite base class

		self.points = 0 #This is the amount of points the robot has in total
		self.location = 0 #where on treasure sort map robot is
		self.image = pygame.image.load('ASSETS/car.png') #loads image
		self.rect = self.image.get_rect() #gets the rect of the images
		self.rect.x = 0 #stores the x location of the robot on screen
		self.rect.y = 0 #stores the y location of the robot on screen
		self.carrying = "" #stores treasure robot is moving
		self.carryingSwap = "" # stores old object while we replace them
		self.loaded = False #is the robot crrying a treasure?
		self.target = 0 #where on the list is the robot aimed?

	def moveLeft(self):
		if(self.loaded == False):
			#for i in range(0,28): #moves 140 pixels
			self.rect.x -= 5 #left 2 pixels
				#screen.blit(background, (0, 0)) #makes the background blit
				#self.update() #updates something else
				#for i in treasureList: #goes through the treasures argh
					#i.update() #updates that too
				#pygame.display.update() #updates the screen
				#time.sleep(0.001) #go to sleep pygame
			self.location = self.location - 1 #change the array location
		elif(self.loaded == True):
			#for i in range(0,28): #moves 140 pixels
			self.rect.x -= 5 #left 2 pixels
			self.carrying.rect.x = self.rect.x
			self.carrying.rect.y = self.rect.y
				#screen.blit(background, (0, 0)) #makes the background blit
				#self.update() #updates something else
				#self.carrying.update()
				#for i in treasureList: #goes through the treasures argh
				#	i.update() #updates that too
				#pygame.display.update() #updates the screen
				#time.sleep(0.001) #go to sleep pygame
			self.location = self.location - 1 #change the array location

	def moveRight(self): #moves robot right
		if(self.loaded == False):
			#for i in range(0,28): #moves for 140 pixels (one block yeah)
			self.rect.x += 5 #right two pixels
				#screen.blit(background, (0, 0)) #blit the background
				#self.update() #updates the screen bro
				#for i in treasureList: #loops through the treasures, this is bad code
				#	i.update() #update them dubbloons
				#pygame.display.update() #shove that to the screen please
				#time.sleep(0.001) #GO TO SLEEP PLEASE 
			self.location = self.location + 1 #change the location in array
		elif(self.loaded == True):
			#for i in range(0,28): #moves 140 pixels
			self.rect.x += 5 #left 2 pixels
			self.carrying.rect.x = self.rect.x
			self.carrying.rect.y = self.rect.y
				#screen.blit(background, (0, 0)) #makes the background blit
				#self.update() #updates the robot
				#self.carrying.update()
				#for i in treasureList: #goes through the treasures argh
				#	i.update() #updates that too

				#pygame.display.update() #updates the screen
				#time.sleep(0.001) #go to sleep pygame
			self.location = self.location + 1 #change the array location
		
