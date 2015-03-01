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
from pygame.locals import * #we need this local so we can run the quit sequence
import sys #again used to run quick sequence
import display #used for p1, p2

#MODULES FOR PART 1
import wikipedia #displays  treasure information
#MODULES FOR PART 2
import random #needed to choose trap


<<<<<<< HEAD
=======

>>>>>>> d3e12b9ff8e11b8f0f8cd2ef478b77f606c7a781
def main():
	pygame.init() #initialise pygame
	screen = display.display()
	clock = pygame.time.Clock() #we will need this for ade's timer

<<<<<<< HEAD
=======
    #Here we will create a new map selection instance.
    #Then we will retrive the data from that to use later.

    #Create a new collector bot. Relies on having an already created City, arena, wishlist and treasurelist.
    cBot = collectorBot(city.arena, city.getWishlist(), city.retTreasureList())
    
    #Create a new instance of a display - For the collector bot thingy
    screen = display.display(city.getImage())   #Passes the image of the city as the background. Requires an instance of city to have been created.
    screen.setCollectorBot(cBot.returnlocationX(), cBot.returnLocationY(), cBot.returnImage()) #Set the location for the collector bot. Requires a location of a new bot to have been specified.
>>>>>>> d3e12b9ff8e11b8f0f8cd2ef478b77f606c7a781

