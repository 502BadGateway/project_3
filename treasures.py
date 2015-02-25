#Treasures class. Inherits from entity class.



class treasure(entity):
	def __init__(self):
		self.sortListLocation = 0 
		#This is for the sortBot to know where it is on inventory list.
		#You need to change this var after you have called swap(n,m)
		#to the new location of the file.
		#maybe I will add that to the swap function. 
		#ask me, i am thiking in code areas.

