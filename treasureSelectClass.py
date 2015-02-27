import pygame

white = (255,255,255)

class treasureSelect():
    
#set display
    def treasurePanel(self):
    	pygame.init()
        screen = pygame.display.set_mode((510, 320)) 
        screen.fill((white))

#load all images
        self.Crown = pygame.image.load("ASSETS\Crown.PNG")
        self.Orb = pygame.image.load("ASSETS\Orb.PNG")
        self.Tierrah = pygame.image.load("ASSETS\Tierrah.PNG")
        self.Sword = pygame.image.load("ASSETS\Sword.PNG")
        self.Ring = pygame.image.load("ASSETS\Ring.PNG")
        self.Coin = pygame.image.load("ASSETS\Coin.png")


#make all images same size
        self.Crown = pygame.transform.scale(self.Crown,(130,100))
        self.Orb = pygame.transform.scale(self.Orb,(130,100))
        self.Tierrah = pygame.transform.scale(self.Tierrah,(30,100))
        self.Sword = pygame.transform.scale(self.Sword,(130,100))
        self.Ring = pygame.transform.scale(self.Ring,(130,100))
        self.Coin = pygame.tran

        self.C = self.display.blit(self.Crown,(30,40))
        self.O = self.display.blit(self.Orb,(190,40))
        self.T = self.display.blit(self.Tierrah,(350,40))
        self.S = self.display.blit(self.Sword,(30,180))
