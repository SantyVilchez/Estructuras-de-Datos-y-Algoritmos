from nodo_contacto import Contacto
class ListaEncadenada:
    __cabeza : Contacto
    __cant : int
    def __init__(self):
        self.__cabeza = None
        self.__cant = 0
    def vacia(self):
        return self.__cant == 0
    def insertar(self,nombre:str,telefono:int):
        nuevo = Contacto(nombre,telefono)
        if self.__cant:
            anterior = None
            actual = self.__cabeza
            while actual != None and actual.getNombre() < nombre:
                anterior = actual
                actual = actual.getSig()
            if anterior:
                nuevo.setSig(anterior.getSig())
                anterior.setSig(nuevo)
            else:
                nuevo.setSig(self.__cabeza)
                self.__cabeza = nuevo
        else:
            self.__cabeza = nuevo
        self.__cant += 1
    def suprimirPorPosicion(self,posicion:int):
        if 1 <= posicion <= self.__cant:
            if not self.vacia():
                posicion -= 1
                indice = 0
                anterior = None
                actual = self.__cabeza
                while indice != posicion:
                    anterior = actual
                    actual = anterior.getSig()
                    indice += 1
                if anterior:
                    anterior.setSig(actual.getSig())
                else:
                    self.__cabeza = actual.getSig()
                self.__cant-=1
            else:
                print("La lista esta vacia")
        else:
            print("indice fuera de rango")
    def recorrer(self):
        aux = self.__cabeza
        print("Lista de Contactos")
        while aux != None:
            print(f"Nombre: {aux.getNombre()} Numero de Telefono: {aux.getTelefono()}")
            aux = aux.getSig()
    def buscar(self,elemento):
        encontrado = False
        aux = self.__cabeza
        while aux != None and aux.getNombre() != elemento:
            aux = aux.getSig()
        if aux:
            encontrado = True
        return encontrado
    def inciso_1(self):
        nombre = input("Ingrese nombre del contacto: ")
        telefono = int(input("Ingrese numero de telefo del contacto: "))
        if self.buscar(nombre):
            print("El Contacto ya existe en la lista ")
        else:
            self.insertar(nombre,telefono)
            print("El Contacto fue agendado con exito!")
    def inciso_2(self):
        nombre = input("Ingrese El nombre del contacto a eliminar: ")
        if self.buscar(nombre):
            if not self.vacia():
                anterior = None
                actual = self.__cabeza
                while actual != None and actual.getNombre() != nombre:
                    anterior = actual
                    actual = anterior.getSig()
                if anterior:
                    anterior.setSig(actual.getSig())
                else:
                    self.__cabeza = actual.getSig()
                self.__cant-=1
                print("El contacto fue eliminado de la agenda")
            else:
                print("La lista esta vacia")
        else:
            print("indice fuera de rango")
    def inciso_3(self):
        nombre = input("Ingrese El nombre del contacto a eliminar: ")
        aux = self.__cabeza
        while aux != None and aux.getNombre() != nombre:
            aux = aux.getSig()
        if aux != None:
            print(f"El contacto {nombre} tiene el telefo {aux.getTelefono()}")
        else:
            print("No existe el contacto ")

 