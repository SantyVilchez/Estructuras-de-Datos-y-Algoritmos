from nodo_lista import Cancion
class ListaEncadenada:
    __cabeza : Cancion
    __cant : int
    def __init__(self):
        self.__cabeza = None
        self.__cant = 0
    def vacia(self):
        return self.__cant == 0
    def suprimirPorPosicion(self,posicion:int):
        if 0 <= posicion <= self.__cant:
            if not self.vacia():
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
        c = 0
        while aux != None:
            print(f"[{c}] {aux.getcancion()}")
            aux = aux.getSig()
            c+=1
    def buscar(self,elemento):
        encontrado = False
        aux = self.__cabeza
        while aux != None and aux.getNombre() != elemento:
            aux = aux.getSig()
        if aux:
            encontrado = True
        return encontrado
    def inciso_1(self):
        cancion = input("Ingrese Cancion: ")
        nuevo = Cancion(cancion)
        aux = self.__cabeza
        if aux:
            while aux.getSig() != None:
                aux = aux.getSig()
            aux.setSig(nuevo)
        else:
            self.__cabeza = nuevo
        self.__cant+=1
    def inciso_2(self):
        posicion = int(input("Ingrese la posicion en la que quieres insertar: "))
        cancion = input("Ingrese la cancion a ingresar: ")
        nuevo = Cancion(cancion)

        anterior = None
        actual = self.__cabeza
        indice = 0
        if 0 <= posicion <= self.__cant:
            while indice != posicion:
                anterior = actual
                actual = actual.getSig()
                indice +=1
            anterior.setSig(nuevo)
            nuevo.setSig(actual)
        else:
            print("Indice Fuera de rango")
    def inciso_3(self):
        posicion = int(input("Ingrese la posicion para ver que cancion esta: "))
        if 0 <= posicion <= self.__cant:
            if not self.vacia():
                indice = 0
                actual = self.__cabeza
                while indice != posicion:
                    actual = actual.getSig()
                    indice += 1
                print(f"El elemento en la posicion {posicion} es {actual.getcancion()}")
            else:
                print("La lista esta vacia")
        else:
            print("indice fuera de rango")
    def inciso_4(self):
        cancion = input("Ingrese la cancion para ver su posicion: ")
        aux = self.__cabeza
        posicion = 0
        while aux != None and aux.getcancion() != cancion:
            aux = aux.getSig()
            posicion += 1
        if aux:
            print(f"La posicion del la cancion {aux.getcancion()} es {posicion}")
        else:
            print("El elemento no se encuentra en la lista")
    def inciso_5(self):
        posicion = int(input("Ingrese la posicion del elemento a eliminar: "))
        self.suprimirPorPosicion(posicion)