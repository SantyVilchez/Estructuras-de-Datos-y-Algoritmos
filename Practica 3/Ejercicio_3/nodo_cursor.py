class Nodo:
    __cabeza:str
    __siguiente: int

    def __init__(self):
        self.__cabeza = None
        self.__siguiente = None

    def getSiguiente(self) -> int:
        return self.__siguiente
    
    def setSiguiente(self,x) -> None:
        self.__siguiente = x
    
    def getDato(self) -> str:
        return self.__cabeza
    
    def setDato(self,x) -> None:
        self.__cabeza = x