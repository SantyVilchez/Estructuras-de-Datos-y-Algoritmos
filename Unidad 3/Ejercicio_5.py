import numpy as np
class ColaSecuencial:
    __Pr : int
    __Ul: int
    __max: int
    __cant:int 
    def __init__(self,maximo : int):
        self.__lista = np.empty(maximo,dtype=int)
        self.__Pr = -1
        self.__Ul = -1
        self.__max = maximo
        self.__cant = 0
    def GetPrimero(self):
        return self.__Pr
    def GetCantidad(self):
        return self.__cant
    def llena(self):
        return self.__cant == self.__max
    def vacia(self):
        return self.__cant == 0
    def insertar(self,elem:int):
        if not self.llena():
            if self.vacia():
                self.__Pr = self.__Ul = (self.__Ul + 1) % self.__max
                self.__lista[self.__Ul] = elem
            else:
                self.__Ul = (self.__Ul +1) % self.__max
                self.__lista[self.__Ul] = elem
            self.__cant += 1
        else:
            print(f"La pila se lleno por lo tanto el elemento {elem} no pudo ser insertado")
    def suprimir(self):
        if self.vacia():
            return 0
        else:
            borrado = self.__lista[self.__Pr]
            self.__Pr = (self.__Pr + 1) % self.__max
            self.__cant -= 1
            return borrado
    def recorrer(self):
        if not self.vacia():
            i = self.__Pr
            j = 0
            while j < self.__cant:
                print(self.__lista[i])
                i = (i + 1) % self.__max
                j += 1

class Celda:
    __elem : int
    __sig : None
    def __init__(self,elem):
        self.__elem = elem
        self.__sig = None
    def getElem(self):
        return self.__elem
    def setElem(self,elem):
        self.__elem = elem
    def getSig(self):
        return self.__sig
    def setSig(self,sig):
        self.__sig = sig
class ColaEncadenada:
    __primero : Celda
    __ultimo : Celda
    __cant : int
    def __init__(self):
        self.__primero = None
        self.__ultimo = None
        self.__cant = 0
    def vacia(self):
        return self.__cant == 0
    def insertar(self,elem : int):
        nuevo = Celda(elem)
        if self.vacia():
            self.__primero = nuevo
        else:
            self.__ultimo.setSig(nuevo)
        self.__ultimo = nuevo
        self.__cant += 1
    def suprimir(self):
        if self.vacia():
            return 0
        else:
            suprimido = self.__primero.getElem()
            self.__cant -= 1
            self.__primero = self.__primero.getSig()
            return suprimido
    def recuperar(self)->Celda:
        return self.__primero
    def recorrer(self):
        aux = self.__primero
        while aux != None:
            print(aux.getElem())
            aux = aux.getSig()
    
if __name__ == '__main__':
    print("Cola Secuencial")
    ColaS = ColaSecuencial(5)
    ColaS.insertar(1)
    ColaS.insertar(2)
    ColaS.insertar(3)
    ColaS.insertar(4)
    ColaS.insertar(5)
    ColaS.insertar(6)
    ColaS.recorrer()
    print("Cola Encadenada")
    ColaE = ColaEncadenada()
    ColaE.insertar(1)
    ColaE.insertar(2)
    ColaE.insertar(3)
    ColaE.insertar(4)
    ColaE.insertar(5)
    ColaE.insertar(6)
    ColaE.recorrer()
    print("Primer Elemento en la Cola es ",ColaE.recuperar().getElem())
    ColaE.suprimir()
    ColaE.suprimir()
    ColaE.suprimir()
    print("Luego desuprimir 3 primeros")
    ColaE.recorrer()