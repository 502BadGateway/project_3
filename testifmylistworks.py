import pygame

class treasure(pygame.sprite.Sprite): #I mocked up a treasure class, we can pull it from the other one

	def __init__(self): #initialise it
		pygame.sprite.Sprite.__init__(self) #no idea why i need it, but i need it
		self.name = "" #give that dubbloon a name
		self.image = pygame.image.load('ASSETS/testTreasure.png') #and a picture
		self.rect = self.image.get_rect() #get yourself a rectangle
		self.rect.x = 0 #x coord of the treasure
		self.rect.y = 0 #y coord of the treasure
		self.points = 0 #points the treasure is worth
		self.location = 0 #location in list yeah
		self.locationInListX = 0
		self.locationInListY = 0

	def update(self): #update it
		screen.blit(self.image, (self.rect.x, self.rect.y)) #blit that dubbloon


class Null(treasure): #nt sure if i will need this when we intergreate

	def update(self): #but it works, when this is in the list, we dont bug out when we
		return None #run i.update()

null = Null() #makes the null object for the list!
"""
THE TREASURES 

This code is only needed for this file.
I wont actually use the majority of it, it will be pulled from phil/femi code.

This will be a list of treasures pulled from the collectorBot.
collectorBot inventory will be 7 treasures.
"""

treasure0 = treasure()  #ALL THIS ISNT NEEDED I DONT THINK
treasure0.name = "CLIVE!"
treasure0.location = 1  #make the treasure location 5 in list

treasure1 = treasure() #create object treasure2
treasure1.location = 0 #put treasure 2 in slot 3

treasure2 = treasure() #create object treasure3
treasure2.location = 2 #put treasure 3 in slot 1

treasure3 = treasure() #create object treasure4
treasure3.location = 3 #put it in slot 2 please

treasure4 = treasure() #create object treasure5
treasure4.location = 4 #put it in slot 5

treasure5 = treasure() #ok so you get the point, but i want the lines on the github
treasure5.location = 5 #gunna look like i wrote so much code son

treasure6 = treasure() #I mean, just give me my degree already
treasure6.location = 6 #place treasure 7 in slot 4

treasureList = []

initialList = [treasure0, treasure1, treasure2, treasure3, treasure4, treasure5, treasure6]
for i in initialList:
	if i.location == i:
		treasureList.append[i]

print initialList
print treasureList