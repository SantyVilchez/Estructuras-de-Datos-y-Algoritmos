class Contacto:
    __nombre : str
    __telefono : int
    __sig : None
    def __init__(self,nombre : str,telefono : int)->None:
        self.__nombre = nombre
        self.__telefono = telefono
        self.__sig = None
    def getNombre(self)->int:
        return self.__nombre
    def setNombre(self,nom:str)->None:
        self.__nombre = nom
    def getTelefono(self):
        return self.__telefono
    def setTelefono(self,tel:int):
        self.__telefono = tel
    def getSig(self)->object:
        return self.__sig
    def setSig(self,sig : object)->None:
        self.__sig = sig
