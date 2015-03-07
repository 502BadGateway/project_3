from robot import Robot
import time
import random
#Landmark1 - London
#Landmark2 - Paris
#Landmark3 - Johnasaburgg
#Landmark4 - Tokyo
#Landmark5 - New York
#Landmark6 - Trap

class collectorBot(Robot):      #Class for the collector robot. Inherits from the super class robot.
    def __init__(self, arena, wishList, treasureList, x, y):
        Robot.__init__(self,"ASSETS/car.png","Barry",x, y)
    
        self.__wishlist = set(wishList)#Define with wishlist and inventory varS
        self.__inventory = [] 
        self.__treasureList = treasureList 
        self.targetX = 0
        self.targetY = 0

        self.__points = 0
    
    def treasureCheck(self, arena, treasureList): #checks for treasures around this location. TODO Should make sure that Phil knows what order this funtion expects the treasures in.
        wishlist = treasureList #Cos who knows where the actual wish list is meant to be coming from.
        collected = False

        for treasure in treasureList:        #For every item  in the list of treasures
            for items in wishlist:
                if collected == True:
                    break
                if treasure.getName() == items.getName():
                    if self.returnLocationX() -2 <= treasure.returnLocationX() <= self.returnLocationX()+2 and self.returnLocationY()-2 <= treasure.returnLocationY() <=  self.returnLocationY()+2: #If we are, then see if they're in our wishlist
                        print "found treasure"
                        self.__inventory.append(treasure)       #If so then add them to the inventory
                        self.__points += 1                      #And add to the score
                        treasure.setCollected(True)
                        collected = True
            
    
        return collected

    def trapCheck(self, arena, trapLandmark6): #this is a trap check which works in a similar way as the treasure check
      if arena.ret_element_val(self.locationX,self.locationY) == trapLandmark6:
        print "You have come across a trap!"
        self.__inventory.pop()
        self.__points -= 1
      else:
        print "There are no Traps here!"



    def updateLocation(self, city, arena, bot, target):
        self.targetX = target[0]
        self.targetY = target[1]


        if bot.returnLocationX() > self.targetX:
            self.moveDown(arena)
            return

        elif self.returnLocationX() < self.targetX:
            self.moveRight(arena)
            return

        if self.returnLocationY() > self.targetY:
            self.moveLeft(arena)
            return
        elif self.returnLocationY() < self.targetY:
            self.moveRight(arena)
            return


    def ret_points(self):
        return self.__points
        
##TIME VARIABLE
##user inputs time in minutes and seconds
#minutes = input("How many minutes: ") 
#seconds = input("Number of seconds: ")
#
#startTime = time.time()
#finishTime = startTime + seconds
#
#count = 0
#
#while time.time() < finishTime:
#  count += 1
#  print count
#  time.sleep(1) #sleep for a second
#
#print "Time is up!"  



