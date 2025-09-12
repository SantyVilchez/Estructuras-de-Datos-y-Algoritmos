#Esta hard esta mrd 

# from nodo_cursor import Nodo
# import numpy as np
# class Registro:
#     __arreglo= np.ndarray
#     __cant = int
#     __disponible = int
#     __tamaño = int
#     __primero = int
#     def __init__(self,tamaño):
#         self.__cant = 0
#         self.__disponible = 0
#         self.__tamaño = tamaño
#         self.__arreglo = np.empty(tamaño,dtype=Nodo)
#         self.__primero = 0
#         for x in range(tamaño):
#             self.__arreglo[x]=Nodo()
#             if x != tamaño-1:
#                 self.__arreglo[x].setSiguiente(x+1)
#             else:
#                 self.__arreglo[x].setSiguiente(-1)

#     def vacia(self):
#         return self.__cant == 0
#     def llena(self):
#         return self.__cant == self.__tamaño
#     def longitud(self):
#         return self.__cant

#     def mostrar(self):
#         indice = self.__primero
#         x = 0
#         while x < self.__cant:
#             print(self.__arreglo[indice].getDato())
#             indice = self.__arreglo[indice].getSiguiente()
#             x+=1
#     def insertar(self,elemento : str):
#         if not self.llena():
#             self.__arreglo[self.__disponible].setDato(elemento)
#             ultimo_insertado = self.__disponible
#             self.__disponible = self.__arreglo[self.__disponible].getSiguiente()
#             self.__cant += 1
#             if self.longitud()>1:
#                 anterior = None
#                 actual = self.__primero
#                 while self.__arreglo[actual].getDato() != None and self.__arreglo[actual].getDato() < elemento:
#                     anterior = actual
#                     actual = self.__arreglo[actual].getSiguiente()
#                 self.__arreglo[ultimo_insertado].setSiguiente(self.__arreglo[actual].getSiguiente())
#                 self.__arreglo[anterior].setSiguiente(ultimo_insertado)
#             return elemento
#         else:
#             print("La lista esta llena.")

# if __name__=="__main__":
#     Registro_1 = Registro(5)
#     Registro_1.insertar("a")
#     Registro_1.insertar("c")
#     Registro_1.mostrar()