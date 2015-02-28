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

        font = pygame.font.Font(None,20)
        text = font.render("Please Select 3 treasures you would like to be collected",1(10,10,10))
        slef.display.blit(text, (28,12))

        pygame.display.flip()

        i=0
        while i < 4:
        	for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

				#detects which button the user has clicked on
				elif event.type == pygame.MOUSEBUTTONDOWN: 
					x, y = event.pos
					#print "click",x,y
					if  x>30 and x<160 and y>40 and y<140:
						print "Crown Clicked"
					elif x>190 and x<320 and y>40 and y<140:
						print "Orb Clicked"
					elif x>350 and x<480 and y>40 and y<140:
						print "Tierrah Clicked"
					elif x>30 and x<160 and y>180 and y<280:
						print "Sword Clicked
					elif x>190 and x<320 and y>180 and y<280:
						print "Ring Clicked"
					elif x>350 and x<480 and y>180 and y<280:
						print "Coin Clicked"
					else:
						print "not on button" 
