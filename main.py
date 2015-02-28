 """

Ive recreated this file because the original main file was straight from project 2.
No attempt to clean up, add new functionality or adapt current has been made. 
Importing modules we arnt using, and using stuff we agreed not to use.
After going through it, its quicker to c/p back in stuff we need, rather than modify it.
Since its quicker to write code than to read it.

- Dan

"""
#ALL PROJECT MODULES
import pygame #We need this to run anything
from pygame.locals import * #we need this local so we can run the quit sequence
import sys #again used to run quick sequence
import display #used for p1, p2 and p3

#MODULES FOR PART 1
import wikipedia #displays  treasure information
#MODULES FOR PART 2
import random #needed to choose trap

def main():
	pygame.init() #initialise pygame
	clock = pygame.time.Clock() #we will need this for ade's timer

