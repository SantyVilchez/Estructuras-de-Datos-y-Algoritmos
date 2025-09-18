class Nodo:
    __valor : int
    __izq : object
    __der : object
    def __init__(self, valor : int):
        self.__valor = valor
        self.__izq = None
        self.__der = None
    def setValor(self,new : int):
        self.__valor = new
    def getValor(self):
        return self.__valor
    def setIzq(self,new : object):
        self.__izq = new
    def getIzq(self):
        return self.__izq
    def setDer(self,new : object):
        self.__der = new
    def getDer(self):
        return self.__der