class Celda:
    __elem : str
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
class Cola:
    __primero : Celda
    __ultimo : Celda
    __cant : int
    def __init__(self):
        self.__primero = None
        self.__ultimo = None
        self.__cant = 0
    def vacia(self):
        return self.__cant == 0
    def insertar(self,elem : str):
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