class Nodo:
    __elem : int
    __sig : None
    def __init__(self,elem : int)->None:
        self.__elem = elem
        self.__sig = None
    def getElem(self)->int:
        return self.__elem
    def setElem(self,elem)->None:
        self.__elem = elem
    def getSig(self)->object:
        return self.__sig
    def setSig(self,sig : object)->None:
        self.__sig = sig

class ListaEncadenada:
    __cabeza : Nodo
    __cant : int
    def __init__(self):
        self.__cabeza = None
        self.__cant = 0
    def vacia(self):
        return self.__cant == 0
    def insertar(self,elem:int):
        nuevo = Nodo(elem)
        if self.__cabeza is None or elem < self.__cabeza.getElem():
            nuevo.setSig(self.__cabeza)
            self.__cabeza = nuevo
        else:
            anterior = self.__cabeza
            while anterior.getSig() != None and elem > anterior.getSig().getElem():
                anterior = anterior.getSig()
            nuevo.setSig(anterior.getSig())
            anterior.setSig(nuevo)
        self.__cant += 1
    def suprimir(self):
        self.__cant-=1 
        borrado = self.__cabeza 
        self.__cabeza = self.__cabeza.getSig() 
        return borrado 
    def recorrer(self):
        aux = self.__cabeza
        while aux != None:
            print(aux.getElem())
            aux = aux.getSig()
