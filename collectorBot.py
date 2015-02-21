import robot.py


class collectorBot(robot):      #Class for the collector robot. Inherits from the super class robot.
  def__init__(self):
    self.score = 0
    self.treasure = ("London", "Johnasabergg", "New York", "Paris", "Tokyo")
   
    if answerinput.touch() in treasure:
      print ("You've found the Treasure!")
      score + 1

    else:
     print ("That is a Trap!...")
     score - 1
    print (score)
