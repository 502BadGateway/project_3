import pygame

white = (255,255,255)

class treasureSelect():
    pygame.init()
#set display
    def set_display(self):
        screen = pygame.display.set_mode((640, 480)) 
        screen.fill((white))

#load all images
    def set_image(self):
        self.Crown = pygame.image.load("Crown.PNG")
        self.Orb = pygame.image.load("Orb.PNG")
        self.Tierrah = pygame.image.load("Tierrah.PNG")
        self.Sword = pygame.image.load("Sword.PNG")
        self.Ring = pygame.image.load("Ring.PNG")


#make all images same size
    def set_size(self):
        self.Crown = pygame.transform.scale(self.Crown,(120,100))
        self.Orb = pygame.transform.scale(self.Orb,(120,100))
        self.Tierrah = pygame.transform.scale(self.Tierrah,(120,100))
        self.Sword = pygame.transform.scale(self.Sword,(120,100))
        self.Ring = pygame.transform.scale(self.Ring,(120,100))
