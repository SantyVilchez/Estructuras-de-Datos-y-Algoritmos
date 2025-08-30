import numpy as np
class PilaSecuencial:
    __tope : int
    __max : int
    __items: list
    __cant:int
    def __init__(self,max):
        self.__items = np.empty(max,dtype=int)
        self.__tope = -1
        self.__max = max
        self.__cant = 0
    def GetTope(self):
        return self.__tope
    def GetCantidad(self):
        return self.__cant
    def llena(self):
        return self.__cant==self.__max
    def vacia(self):
        return self.__tope ==-1
    def insertar(self,elem:int):
        if self.llena():
            print("La pila se Lleno")
        else:
            self.__tope += 1
            self.__items[self.__tope]=elem
            self.__cant+=1
    def suprimir(self):
        if self.vacia():
            print("La Lista esta vacia")
        else:
            borrado = self.__items[self.__tope]
            self.__tope-=1
            return borrado
class Celda:
    __elem:int
    __sig:None
    def __init__(self,elem:int):
        self.__elem = elem
        self.__sig = None
    def getSig(self):
        return self.__sig
    def setSig(self,sig):
        self.__sig = sig
    def getElem(self):
        return self.__elem
class PilaEncadenada:
    __tope : Celda
    __cant : int
    def __init__(self):
        self.__tope = None
        self.__cant = 0
    def insertar(self,elem:int):
        aux  = Celda(elem)
        aux.setSig(self.__tope)
        self.__tope = aux
        self.__cant += 1
    def suprimir(self):
        self.__cant-=1
        borrado = self.__tope.getElem()
        self.__tope = self.__tope.getSig()
        return borrado
    def vacia(self):
        return self.__cant == 0
    def recorrer(self):
        aux = self.__tope
        while aux != None:
            print(aux.getElem())
            aux = aux.getSig()
    def cantidad(self):
        return self.__cant
    def tope(self):
        return self.__tope.getElem()
    def grafico(self):
        aux= self.__tope
        while aux!=None:
            print(aux.getElem())
            aux = aux.getSig()
if __name__ == '__main__':
    pilaS = PilaSecuencial(4)
    pilaE = PilaEncadenada()
    print("Pila Secuencial")
    pilaS.insertar(1)
    pilaS.insertar(2)
    pilaS.insertar(3)
    pilaS.insertar(4)
    pilaS.insertar(5)
    while pilaS.vacia() != True:
        print(pilaS.suprimir())
    print("Pila Encadenada")
    pilaE.insertar(1)
    pilaE.insertar(2)
    pilaE.insertar(3)
    pilaE.insertar(4)
    pilaE.insertar(5)
    pilaE.recorrer()

