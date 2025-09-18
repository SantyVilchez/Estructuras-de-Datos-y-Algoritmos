class Nodo:
    __valor: int
    __fila: int
    __columna : int
    __sig : None
    def __init__(self,valor: int,fila:int,columna:int)->None:
        self.__valor= valor
        self.__fila = fila
        self.__columna = columna
        self.__sig = None

    def getValor(self)->int:
        return self.__valor
    def setValor(self,valor)->None:
        self.__valor= valor

    def getFila(self)->int:
        return self.__fila
    def setFila(self,fila)->None:
        self.__fila= fila

    def getColumna(self)->int:
        return self.__columna
    def setColumna(self,columna)->None:
        self.__columna= columna

    def getSig(self)->object:
        return self.__sig
    def setSig(self,sig : object)->None:
        self.__sig = sig
