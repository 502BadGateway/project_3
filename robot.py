class Robot: 

    def __init__(self, image, name, x,y): #Constructor - Sets variables.
        import pygame

        self.__image = image 
        self.__name = name 
        self.__points = 0 
        self.__locationX = x
        self.__locationY = y 


    def moveUp(self, arena): #Change the location of the robot to make it move up
        self.locationY -= 1
        arena.put(self.locationX, self.locationY-1)
        self.check()
    def moveDown(self):
        self.locationY += 1
        arena.put(self.locationX, self.locationY+1)
        self.check()
    def moveLeft(self):
        self.locationX += 1
        arena.put(self.locationX-1, self.locationY)
        self.check()
    def moveRight(self):
        self.locationX += 1
        arena.put(self.locationX+1, self.locationY)
        self.check()

    def returnLocationX():  #Return the X location of the bot
        return self.__locationX

    def returnRectY(self):  #Return the Y location of the bot
        return self.__locationY

    def returnPoints(self):
        return self.__points

    def returnImage(self):  #returns image of the robot
        return self.__image



bot = Robot("map.png", "barry", 10, 22)
