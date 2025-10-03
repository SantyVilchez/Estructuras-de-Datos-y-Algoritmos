from nodo_arbol import Nodo
class Nodo_lista:
    __elem : object
    __sig : None
    def __init__(self,elem : Nodo)->None:
        self.__elem = elem
        self.__sig = None
    def getElem(self)->object:
        return self.__elem
    def setElem(self,elem)->None:
        self.__elem = elem
    def getSig(self)->object:
        return self.__sig
    def setSig(self,sig : object)->None:
        self.__sig = sig

class ListaEncadenada:
    __cabeza : Nodo_lista
    __cant : int
    def __init__(self):
        self.__cabeza = None
        self.__cant = 0
    def vacia(self):
        return self.__cant == 0
    def insertar(self,elem:Nodo):
        nuevo = Nodo_lista(elem)
        if self.__cabeza is None or elem.getFrecuencia() < self.__cabeza.getElem().getFrecuencia():
            nuevo.setSig(self.__cabeza)
            self.__cabeza = nuevo
        else:
            anterior = self.__cabeza
            while anterior.getSig() != None and elem.getFrecuencia() > anterior.getSig().getElem().getFrecuencia():
                anterior = anterior.getSig()
            nuevo.setSig(anterior.getSig())
            anterior.setSig(nuevo)
        self.__cant += 1
    def suprimir(self)->Nodo:
        self.__cant-=1 
        borrado = self.__cabeza.getElem() 
        self.__cabeza = self.__cabeza.getSig() 
        return borrado 
    def recorrer(self):
        aux = self.__cabeza
        while aux != None:
            print(aux.getElem().getFrecuencia())
            aux = aux.getSig()
    def cantidad(self):
        return self.__cant
    def cabeza(self):
        return self.__cabeza
