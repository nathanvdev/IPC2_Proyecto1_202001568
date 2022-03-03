
class Pattern:
    def __init__(self, code, patt) -> None:
        self.Code = code
        self.Patt = patt
        self.Next = None

    def setCode(self, code):
        self.Code = code

    def getPatt(self):
        return self.Patt
    
    def setPatt(self, patt):
        self.Patt = patt

    def getCode(self):
        return self.Code
    
    def setNext(self, Pattern):
        self.Next = Pattern
    
    def getNext(self):
        return self.Next


        
    

    
    
    
        