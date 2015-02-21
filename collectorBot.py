import robot.py
#Landmark1 - London
#Landmark2 - Paris
#Landmark3 - Johnasaburgg
#Landmark4 - Tokyo
#Landmark5 - New York
class collectorBot(robot):      #Class for the collector robot. Inherits from the super class robot.
  def__init__(self, arena): 
    
    def treasureCheck(self, arena, treasureLandmark1, treasureLandmark2, treasureLandmark3, treasureLandmark4, treasureLandmark5):
      if self.ret_element_val(self.locationX,self.locationY) == treasureLandmark1: 
        print "Treasure in London Found!"
        self.points += 1 #this adds a point to robot's score

      elif self.ret_element_val(self.locationX,self.locationY) == treasureLandmark2: 
        print "Treasure in Paris Found!"
        self.points += 1

      elif self.ret_element_val(self.locationX,self.locationY) == treasureLandmark3: 
        print "Treasure in Johnasaburgg Found!"
          self.points += 1
          
      elif self.ret_element_val(self.locationX,self.locationY) == treasureLandmark4: 
        print "Treasure in Tokyo Found!"
          self.points += 1      
          
      elif self.ret_element_val(self.locationX,self.locationY) == treasureLandmark5: 
        print "Treasure in New York Found!"
          self.points += 1
      else:
        print "No Treasrue at this landmark"
