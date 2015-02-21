import robot.py
import simplegui
#Landmark1 - London
#Landmark2 - Paris
#Landmark3 - Johnasaburgg
#Landmark4 - Tokyo
#Landmark5 - New York
#Landmark6 - Trap

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
        print "There is no Treasrue at this landmark"
        
    def trapCheck(self, arena, trapLandmark6):
      if self.ret_element_val(self.locationX,self.locationY) == trapLandmark6:
        print "You have come across a trap!"
        self.points -= 1
      else:
        print "There are no Traps here!"
        
# Define global variables
mins, sec, count, x, y, x1, y2 = 0, 0, 0, 0, 0, 0, 0

# counting tenths of seconds into formatted string A:BC.D
    def format(t):
      global count, sec, mins
      t = count   
      
      if (t == 10):
        sec += 1
        count = 0
      if (sec == 60):
        mins += 1
        sec = 0
    def start_timer():
      global x1, y2
      if x1-y2 == 0:
        x1 += 1
        timer.start()

    def stop_timer():
      global x, y, x1, y2
      if x1-y2 == 1:
        y2 += 1
        timer.stop()
        y += 1
      if count == 0 :
        x += 1
    
    def reset_timer():
      global count, sec, mins, x, y, x1,y2
      timer.stop()
      mins, sec, count, x, y,x1,y2 = 0, 0, 0, 0, 0, 0, 0
    
    def exit_timer():
      frame.stop()
