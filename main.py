# """

#Ive recreated this file because the original main file was straight from project 2.
#No attempt to clean up, add new functionality or adapt current has been made. 
#Importing modules we arnt using, and using stuff we agreed not to use.
#After going through it, its quicker to c/p back in stuff we need, rather than modify it.
#Since its quicker to write code than to read it.
#
#- Dan
#
#"""
#ALL PROJECT MODULES
import pygame #We need this to run anything
#from pygame.locals import * #we need this local so we can run the quit sequence
import sys #again used to run quick sequence
from display import display #used for p1, p2
from mapSelection import mapSelect
from city import city
from collectorBot import collectorBot
from display import display
from sortSelect import sortSelect

#MODULES FOR PART 1
import wikipedia #displays  treasure information
#MODULES FOR PART 2
import random #needed to choose trap

def sortSelect (): #defines function
	sortScreen= display(510,320,False) #creates display
	sortButtons = []#created empty list
	sortButtons.append (sortSelect("bubbleSort",30,40,"ASSETS/bubbleSort.png"130,100)) #creates a instance of a class and puts it into the end of the sort buttons list
	sortButtons.append (sortSelect("mergeSort",190,40,"ASSETS/mergeSort.png"130,100))
	
	for btns in sortButtons: #this states for every button in that list it will...
	    displayScreen.addSortSelectBtn(btns) #...display that button
	    
	sortScreen.render()#actually draws the button
	
def main(mapSelect):

	pygame.init() #initialise pygame
	clock = pygame.time.Clock() #we will need this for ade's timer

	#this is temporary, it will use the display class later
	"""
	displayScreen = pygame.display.set_mode((510,320)) 
	displayBackground = pygame.Surface(displayScreen.get_size())
	displayBackground = displayBackground.convert()
	displayBackground.fill((250,250,250))
	displayScreen.blit(displayBackground,(0,0))"""

	displayScreen = display(510,320, False)

        buttons = []

        buttons.append(mapSelect("London",30,40,"ASSETS/London.png",130,100))
	buttons.append(mapSelect("Paris",190,40,"ASSETS/Paris.png",130,100))
	buttons.append(mapSelect("New York",350,40,"ASSETS/New York.png",130,100))
	buttons.append(mapSelect("Tokyo",30,180,"ASSETS/Tokyo.png",130,100))
	buttons.append(mapSelect("Johannesburg",190,180,"ASSETS/Johannesburg.png",130,100))
	buttons.append(mapSelect("Berlin",350,180,"ASSETS/Berlin.png",130,100))

        for btns in buttons:
	    displayScreen.addMapSelectBtn(btns)

	displayScreen.render()

	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			#detects which button the user has clicked on
			elif event.type == pygame.MOUSEBUTTONDOWN: 
				x, y = event.pos
				#print "click",x,y
				if  x>30 and x<160 and y>40 and y<140:
					print "London Clicked"
                                        City = city("London",[])
                                        return City
					#self.mapSelected = "ASSETS\staticmapLondon.png" # what will be referenced later to know what map to use.
					#treasurePos(mapSelected)
				elif x>190 and x<320 and y>40 and y<140:
					print "Paris Clicked"
                                        City = city("Paris", [])
                                        return City
					#mapSelected = "ASSETS\staticmapParis.png"
					#treasurePos(mapSelected)
				elif x>350 and x<480 and y>40 and y<140:
					print "New York Clicked"
                                        City = city("NewYork",[]) 
                                        return City
					#self.mapSelected = "ASSETS\staticmapNewYork.png"
					#treasurePos(mapSelected)
				elif x>30 and x<160 and y>180 and y<280:
					print "Tokyo Clicked"
                                        City = city("Tokyo",[])
                                        return City
					#self.mapSelected = "ASSETS\staticmapTokyo.png"
					#treasurePos(mapSelected)
				elif x>190 and x<320 and y>180 and y<280:
					print "Johannesburg Clicked"
                                        City = city("Johannesburg",[])
                                        return City
					#self.mapSelected = "ASSETS\staticmapJohannesburg.png"
					#treasurePos(mapSelected)
				elif x>350 and x<480 and y>180 and y<280:
					print "Berlin Clicked"
                                        City = city("Berlin",[])
                                        return City
					#self.mapSelected = "ASSETS\staticmapBerlin.png"
					#treasurePos(mapSelected)
				else:
					print "not on button"


	displayScreen = display(False,670,600)

	treasureButtonChest = treasureSelect("Chest",30,40,"ASSETS/chest.png",130,100)
	displayScreen.add
	
	#mapButtonLondon.cityText(None,20,28,12,"Please select your location",(10,10,10))

def collectBot(city, x, y):
    #Here we will create a new map selection instance.
    #Then we will retrive the data from that to use later.
    print city.ret_image_path()

    screen = display(1280, 960, city.ret_image_path())

	#Create a new collector bot. Relies on having an already created City, arena, wishlist and treasurelist.
    cBot = collectorBot(city.arena, [], [], x, y)
	
	#Create a new instance of a display - For the collector bot thingy
	#Passes the image of the city as the background. Requires an instance of city to have been created.
    screen.setCollectorBot(cBot.returnLocationX(), cBot.returnLocationY(), cBot.returnImage()) #Set the location for the collector bot. Requires a location of a new bot to have been specified.

    while True:
        screen.setCollectorBot(cBot.returnLocationX(), cBot.returnLocationY(), cBot.returnImage()) #Set the location for the collector bot. Requires a location of a new bot to have been specified.
        screen.render()
    

City = main(mapSelect)
collectBot(City, 0, 02)
