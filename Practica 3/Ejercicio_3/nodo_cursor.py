class Nodo:
    __elemento:int
    __siguiente: int

    def __init__(self):
        self.__elemento = None
        self.__siguiente = -1
    def getSiguiente(self) -> int:
        return self.__siguiente
    
    def setSiguiente(self,x) -> None:
        self.__siguiente = x
    
    def getDato(self) -> str:
        return self.__elemento
    
    def setDato(self,x) -> None:
        self.__elemento = x