#File for Sam's heap sort


import sort



class node: #Class for nodes of the tree
    def __init__(self, parent, child, value):
        self.parent = None
        self.child = None
        self.value = None

class heapSort(sort.Sorter):

    def __init__(self, lst):

        self__heap  = []

        noItems = len(lst)

        self.__heap = []

        previousNode = None
        childNode = None
        
        for x in range(0, noItems):
            if x != 0:
                self.__heap[x] = node(parentNode, None, lst[x]) #Create new node with parent node specified and child node not.
                self.__heap[x-1].child = self.__heap[x]         #Set previous child node to above node
            else:
                self.__heap[x] = node(None, None, lst[x])       #If root node, do special things.

            parentNode = self.__heap[x]                         #Set parent node to the node we just created


