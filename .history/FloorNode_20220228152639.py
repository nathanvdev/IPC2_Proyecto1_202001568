class Floor:
    def __init__(self, name, row, column, flip, slide ):
        self.Name = name
        self.Row = row
        self.Column = column
        self.FlipCost = flip
        self.SlideCost = slide
        self.Next = None