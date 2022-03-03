class Cell:
    def __init__(self, posX, posY, color):
        self.PosX = posX
        self.PosY = posY
        self.Color = color
        self.Prev = None
        self.Next = None

    