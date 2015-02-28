#Class file for trap class. Should inherit from entity class.


class trap(entity):

    entity.__init__(self, name, val) #Call the base class constructor. This is because this constructor should be extending not replacing functionality in entity._init__. 
                                     #See here for information on this: Paragraph 6  https://docs.python.org/2/tutorial/classes.html#inheritance
