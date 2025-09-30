from nodo_cursor import Nodo
import numpy as np
class ListaConCursores:
    __arreglo = np.ndarray
    __cant = int
    __disponible = int
    __tamaño = int
    __primero = int
    def __init__(self,tamaño):
        self.__disponible = 0
        self.__tamaño = tamaño
        self.__arreglo = np.empty(tamaño,dtype = Nodo)
        self.__primero = -1
        self.__cant = 0
        for x in range(tamaño):
            self.__arreglo[x] = Nodo()
            if x != tamaño-1:
                self.__arreglo[x].setSiguiente(x+1)
            else:
                self.__arreglo[x].setSiguiente(-1)
    def vacia(self):
        return self.__primero == -1
    def llena(self):
        return self.__disponible == -1
    def mostrar(self):
        indice = self.__primero
        while indice != -1:
            print(f"indice[{indice}]",self.__arreglo[indice].getDato(),"  ",self.__arreglo[indice].getSiguiente())
            indice = self.__arreglo[indice].getSiguiente()
    def insertar(self,elemento : int):
        if not self.llena():
            self.__arreglo[self.__disponible].setDato(elemento)
            self.__disponible = self.__arreglo[self.__disponible].getSiguiente()
            self.__cant += 1
            return elemento
        else:
            print("La lista esta llena.")
    def insertarPorContenido(self,elemento : int):
        if not self.llena():
            nuevo = self.__disponible
            self.__disponible = self.__arreglo[self.__disponible].getSiguiente()
            self.__arreglo[nuevo].setDato(elemento)
            self.__arreglo[nuevo].setSiguiente(-1)
            if self.__primero == -1 or elemento < self.__arreglo[self.__primero].getDato():
                self.__arreglo[nuevo].setSiguiente(self.__primero)
                self.__primero = nuevo
            else:
                anterior = self.__primero
                actual = self.__arreglo[anterior].getSiguiente()
                while actual != -1 and elemento > self.__arreglo[actual].getDato():
                    anterior = actual
                    actual = self.__arreglo[actual].getSiguiente()
                self.__arreglo[nuevo].setSiguiente(actual)
                self.__arreglo[anterior].setSiguiente(nuevo)
            self.__cant += 1
        else:
            print("la lista esta llena.")
    def suprimirPorElemento(self,elemento : int):
        if not self.vacia():
            anterior = -1
            actual = self.__primero
            while actual != -1 and elemento != self.__arreglo[actual].getDato():
                anterior = actual
                actual = self.__arreglo[actual].getSiguiente()
            if actual != -1:
                if anterior != -1:
                    eliminado = actual
                    self.__arreglo[anterior].setSiguiente(self.__arreglo[actual].getSiguiente())
                    self.__arreglo[eliminado].setSiguiente(self.__disponible)
                    self.__disponible = eliminado
                else:
                    eliminado = self.__primero
                    self.__primero = self.__arreglo[self.__primero].getSiguiente()
                    self.__arreglo[eliminado].setSiguiente(self.__disponible)
                    self.__disponible = eliminado
                self.__cant -= 1
            else:
                print("El elemento no existe")
        else:
            print("La lista esta vacia")

if __name__ == "__main__":
    Registro_1 = ListaConCursores(5)
    Registro_1.insertarPorContenido(1)
    Registro_1.insertarPorContenido(3)
    Registro_1.insertarPorContenido(3)
    Registro_1.insertarPorContenido(30)
    Registro_1.insertarPorContenido(-2)
    Registro_1.mostrar()
    print("Luego de eliminar el 30")
    Registro_1.suprimirPorElemento(30)
    Registro_1.mostrar()
 