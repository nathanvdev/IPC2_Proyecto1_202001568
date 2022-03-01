from nodoContacto import Contacto

class ListaContactos():
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def AddContact(self, nombre, Ncasa, Ntrabajo, Nmovil):
        NewContact = Contacto(nombre, Ncasa, Ntrabajo, Nmovil)
        self.size += 1
        if self.primero is None:
            self.primero = NewContact
            self.ultimo = NewContact
        else:
            self.ultimo.setSiguiente(NewContact)
            self.ultimo = NewContact
    
    def showContacts(self):
        tmp = self.primero
        for i in range(self.size):
            print(i, 'Nombre:', tmp.Nombre, 'Telefono de Casa:', tmp.Ncasa, 'Telefono de trabajo:', tmp.Ntrabajo, 'Telefono Movil:', tmp.Nmovil)
            tmp = tmp.getSiguiente()


Directorrio = ListaContactos()
Directorrio.AddContact('fernando', 233544, 2342344, 234234)
Directorrio.AddContact('carlos', 24354, 5645456, 76967788)
Directorrio.AddContact('juan', 56745, 745676, 345345345)
Directorrio.AddContact('alex', 23524542, 34563456, 45674576)