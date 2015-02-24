class Robot: 
    def __init__(self, image, name, x,y): #Constructor - Sets variables.
        import pygame

        self.__image = image 
        self.__name = name 
        self.__points = 0 
        self.__rect = Robot.__image.get_rect()
        self.__rect.x = x
        self.__rect.y = y 

    def moveUp(self):   #move robot functions print "up" def moveDown(self):  #move robot functions  
        print "Down"
    def moveLeft(self):  #move robot functions 
        print "left"
    def moveRight(self):  #move robot functions
        print "Right"
    def returnLocationX():  #Return the X location of the bot
        return self.__rect.x

    def returnRectY(self):  #Return the Y location of the bot
        return self.__rect.y

    def returnPoints(self):
        return self.__points



bot = Robot("map.png", "barry", 10, 22)
