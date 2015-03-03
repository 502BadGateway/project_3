#Super class for sorting algorithms

class Sorter:

    def __init__(self):

    def swap(self, valOne, valTwo, lst):
        tmp = None  

        tmp = lst[valOne] # put first val into tmp
        lst[valOne] = list[valTwo] #replace first value with second
        lst[valTwo] = tmp  #replace second value with first

        return lst

