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

#MODULES FOR PART 1
import wikipedia #displays  treasure information
#MODULES FOR PART 2
import random #needed to choose trap


def main(mapSelect,display):

	pygame.init() #initialise pygame
	clock = pygame.time.Clock() #we will need this for ade's timer

	#this is temporary, it will use the display class later
	"""
	displayScreen = pygame.display.set_mode((510,320)) 
	displayBackground = pygame.Surface(displayScreen.get_size())
	displayBackground = displayBackground.convert()
	displayBackground.fill((250,250,250))
	displayScreen.blit(displayBackground,(0,0))"""

	displayScreen = display(False,510,320)

	mapButtonLondon = mapSelect("London",30,40,"ASSETS/London.png",130,100)
	displayScreen.addMapSelectBtn(mapButtonLondon)
	mapButtonParis = mapSelect("Paris",190,40,"ASSETS/Paris.png",130,100)
	displayScreen.addMapSelectBtn(mapButtonParis)
	mapButtonNewYork = mapSelect("New York",350,40,"ASSETS/New York.png",130,100)
	displayScreen.addMapSelectBtn(mapButtonNewYork)
	mapButtonTokyo = mapSelect("Tokyo",30,180,"ASSETS/Tokyo.png",130,100)
	displayScreen.addMapSelectBtn(mapButtonTokyo)
	mapButtonJohannesburg = mapSelect("Johannesburg",190,180,"ASSETS/Johannesburg.png",130,100)
	displayScreen.addMapSelectBtn(mapButtonJohannesburg)
	mapButtonBerlin = mapSelect("Berlin",350,180,"ASSETS/Berlin.png",130,100)
	displayScreen.addMapSelectBtn(mapButtonBerlin)

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


	
	#mapButtonLondon.cityText(None,20,28,12,"Please select your location",(10,10,10))

def collectBot(city):
	#Here we will create a new map selection instance.
	#Then we will retrive the data from that to use later.

        screen = display(city.ret_image(), 1280, 960, "", 10)

	#Create a new collector bot. Relies on having an already created City, arena, wishlist and treasurelist.
	cBot = collectorBot(city.arena, city.getWishlist(), city.retTreasureList())
	
	#Create a new instance of a display - For the collector bot thingy
	screen = display.display(city.getImage())   #Passes the image of the city as the background. Requires an instance of city to have been created.
        screen.setCollectorBot(cBot.returnlocationX(), cBot.returnLocationY(), cBot.returnImage()) #Set the location for the collector bot. Requires a location of a new bot to have been specified.
    

City = main(mapSelect)
collectBot(City)
