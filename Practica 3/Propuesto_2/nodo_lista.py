class Cancion:
    __cancion : str
    __sig : None
    def __init__(self,cancion : str)->None:
        self.__cancion = cancion
        self.__sig = None
    def getcancion(self)->str:
        return self.__cancion
    def setcancion(self,cancion)->None:
        self.__cancion = cancion
    def getSig(self)->object:
        return self.__sig
    def setSig(self,sig : object)->None:
        self.__sig = sig