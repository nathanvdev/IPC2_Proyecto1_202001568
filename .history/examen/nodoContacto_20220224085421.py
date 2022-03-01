class Contacto():
    def __init__(self, nombre, Ncasa, Ntrabajo, Nmovil):
        self.Nombre = nombre
        self.Ncasa = Ncasa
        self.Ntrabajo = Ntrabajo
        self.Nmovil = Nmovil
        self.siguiente = None

    def setSiguiente(self, tmp):
        self.siguiente = tmp