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
