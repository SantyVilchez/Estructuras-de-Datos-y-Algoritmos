# import numpy as np
# class PilaSecuencial:
#     __tope : int
#     __tamaño : int
#     __lista: list
#     __cantidad:int 
#     def __init__(self,tamaño):
#         self.__lista = np.empty(tamaño,dtype=int)
#         self.__tope = -1
#         self.__tamaño = tamaño
#         self.__cantidad = 1
#     def GetTope(self):
#         return self.__tope
#     def GetCantidad(self):
#         return self.__cantidad
#     def llena(self):
#         return self.__cantidad==self.__tamaño
#     def vacia(self):
#         return self.__tope ==-1
#     def insertar(self,elem:int):
#         if self.llena():
#             print("La pilase Lleno")
#         else:
#             self.__tope += 1
#             self.__lista[self.__tope]=elem
#             self.__cantidad+=1
#     def suprimir(self):
#         if self.vacia():
#             print("La Lista esta vacia")
#         else:
#             print(self.__lista[self.__tope])
#             self.__tope-=1

class PilaSecuencial:
    __cant : int
    __lista= []
    __tope:int
    __tamaño:int
    def __init__(self,tamaño):
        self.__lista = [0] *tamaño
        self.__cant = 0
        self.__tope = -1
        self.__tamaño = tamaño
    def test(self):
        print(self.__lista)
    def insertar(self,elem:int):
        self.__tope+=1
        self.__cant+=1
        self.__lista[self.__tope]=elem

    def suprimir(self):
        if self.vacia()==True:
            print("Vacia")
        else:
            elem =self.__lista[self.__tope]
            print(elem)
            self.__tope-=1
            self.__cant-=1
    def vacia(self):
        return self.__cant == 0
    def recorrer(self):
        for i in range(self.__cant):
            print(self.__lista)
if __name__ == '__main__':
    pila = PilaSecuencial(10)
    pila.test()
    pila.insertar(1)
    pila.insertar(2)
    pila.insertar(3)
    pila.insertar("a")
    while pila.vacia()!= True:
        pila.suprimir()
    