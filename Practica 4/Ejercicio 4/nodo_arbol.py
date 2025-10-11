class Nodo:
    __valor : str
    __contador : int
    __balance : int
    __izq : object
    __der : object
    def __init__(self,valor : int):
        self.__valor = valor
        self.__contador = 1
        self.__balance = 0
        self.__izq = None
        self.__der = None
    def setValor(self,new : int):
        self.__valor = new
    def getValor(self):
        return self.__valor
    def setContador(self, new :int):
        self.__contador = new
    def getContador(self):
        return self.__contador
    def setBalance(self, new : int):
        self.__balance = new
    def getBalance(self):
        return self.__balance
    def setIzq(self,new : object):
        self.__izq = new
    def getIzq(self)->object:
        return self.__izq
    def setDer(self,new : object)->None:
        self.__der = new
    def getDer(self)->object:
        return self.__der