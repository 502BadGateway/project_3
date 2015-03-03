class treasure(entity):

    def __init__(self, x, y, points, name, val, image):
        entity.__init__(self, name, val, image)

        self.__x = x
        self.__y = y

        self.__points = points 
        

    def returnPoints(self):
        return self.__points
    

