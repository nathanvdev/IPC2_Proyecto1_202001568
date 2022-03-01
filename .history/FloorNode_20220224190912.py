class Floor:
    def __init__(self, nombre, r, c, f, s ) -> None:
        self.Nombre = nombre
        self.Row = r
        self.Column = c
        self.FlipCost = f
        self.SlideCost = s
        self.siguiente = None