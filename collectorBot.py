import robot.py
import time
#Landmark1 - London
#Landmark2 - Paris
#Landmark3 - Johnasaburgg
#Landmark4 - Tokyo
#Landmark5 - New York
#Landmark6 - Trap

class collectorBot(robot):      #Class for the collector robot. Inherits from the super class robot.
    def __init__(self, arena, wishList, treasureList):
    
        self.__wishlist = set(wishlist)#Define with wishlist and inventory varS
        self.__inventory = [] 
        self.__treasureList = treasureList 
    
    def treasureCheck(self, arena): #checks for treasures around this location. TODO Should make sure that Phil knows what order this funtion expects the treasures in.


        for treasure in self.__treasureList:        #For every item  in the list of treasures
            if arena.ret_element_val(self.locationX, self.locationY) == treasure.getArenaVal(): #Check if we're on top of them
                if treasure.getArenaValue in self.wishlist: #If we are, then see if they're in our wishlist
                    self.__inventory.append(treasure)       #If so then add them to the inventory
                    self.__points += 1                      #And add to the score
        return

      
#      if self.ret_element_val(self.locationX,self.locationY) == treasureLandmark[0]: 
#        print "Treasure in London Found!"
#        self.__points += 1 #this adds a point to robot's score if it comes across this treasure
#
#      elif arena.ret_element_val(self.locationX,self.locationY) == treasureLandmark[1]: 
#        print "Treasure in Paris Found!"
#        self.__points += 1
#
#      elif arena.ret_element_val(self.locationX,self.locationY) == treasureLandmark[2]: 
#        print "Treasure in Johnasaburgg Found!"
#        self.__points += 1
#          
#      elif arena.ret_element_val(self.locationX,self.locationY) == treasureLandmark[3]: 
#        print "Treasure in Tokyo Found!"
#        self.__points += 1      
#          
#      elif arena.ret_element_val(self.locationX,self.locationY) == treasureLandmark[4]: 
#        print "Treasure in New York Found!"
#        self.__points += 1
#      else:
#        print "There is no Treasrue at this landmark"
        
    def trapCheck(self, arena, trapLandmark6): #this is a trap check which works in a similar way as the treasure check
      if arena.ret_element_val(self.locationX,self.locationY) == trapLandmark6:
        print "You have come across a trap!"
        self.__inventory.pop()
        self.__points -= 1
      else:
        print "There are no Traps here!"
        
#TIME VARIABLE
#user inputs time in minutes and seconds
minutes = input("How many minutes: ") 
seconds = input("Number of seconds: ")

startTime = time.time()
finishTime = startTime + seconds

count = 0

while time.time() < finishTime:
  count += 1
  print count
  time.sleep(1) #sleep for a second

print "Time is up!"  



