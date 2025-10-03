class Nodo:
    __valor : str
    __frecuencia : int
    __izq : object
    __der : object
    def __init__(self, frecuencia:int,valor : str):
        self.__frecuencia = frecuencia
        self.__valor = valor
        self.__izq = None
        self.__der = None
    def setValor(self,new : str):
        self.__valor = new
    def getValor(self):
        return self.__valor
    def setFrecuencia(self, new : int):
        self.__frecuencia = new
    def getFrecuencia(self):
        return self.__frecuencia
    def setIzq(self,new : object):
        self.__izq = new
    def getIzq(self):
        return self.__izq
    def setDer(self,new : object):
        self.__der = new
    def getDer(self):
        return self.__der