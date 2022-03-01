from numpy import flip
from pyparsing import col


class Floor:
    def __init__(self, name, row, column, flip, slide ):
        self.Name = name
        self.Row = row
        self.Column = column
        self.FlipCost = flip
        self.SlideCost = slide
        self.Next = None

    def getName(self):
        return self.Name

    def getRow(self):
        return self.Row
    
    def getColumn(self):
        return self.Column
    
    def getFlipCost(self):
        return self.FlipCost
    
    def getSlideCost(self):
        return self.SlideCost
    
    def getNext(self):
        return self.Next

    def setName(self, name):
        self.Name = name

    def setRow(self, row):
        self.Row = row

    def setColumn(self, column):
        self.Column = column

    def setFlipCost(self, flipcost):
        self.FlipCost = flipcost

    def setSlideCost (self, slidecost):
        self.SlideCost = slidecost
    
    def setNext(self, floor):
        self.Next = floor
        