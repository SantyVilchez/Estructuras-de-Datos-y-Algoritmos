import numpy as np
# Funcion para obtener el primo util para el tamaño de las tablas hash
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def obtener_primo(n):
    if es_primo(n):
        return n
    siguiente = n + 1
    while not es_primo(siguiente):
        siguiente += 1
    return siguiente
# Codigo de Lista enlazada utilizado en la estructura de tabla hash encadenada
class Nodo:
    __elem : str
    __sig : None
    def __init__(self,elem : str)->None:
        self.__elem = elem
        self.__sig = None
    def getElem(self)->str:
        return self.__elem
    def setElem(self,elem)->None:
        self.__elem = elem
    def getSig(self)->object:
        return self.__sig
    def setSig(self,sig : object)->None:
        self.__sig = sig

class ListaEnlazada:
    __cabeza : Nodo
    def __init__(self):
        self.__cabeza = None
    def __str__(self) -> str:
        actual = self.__cabeza
        elementos = []
        while actual:
            elementos.append(str(actual.getElem()))
            actual = actual.getSig()
        return " -> ".join(elementos)
    def insertar(self, valor: str) -> None:
        nuevo = Nodo(valor)
        actual = self.__cabeza
        repetido = False

        if not actual:
            self.__cabeza = nuevo
        else:
            while actual.getSig() != None:
                if actual.getElem() == valor:
                    repetido = True
                actual = actual.getSig()
            if actual.getElem() == valor:
                repetido = True
            if not repetido:
                actual.setSig(nuevo)
    def obtener_cabeza(self):
        return self.__cabeza if self.__cabeza else None

  
# codigo de lista secuencial ordenada por contenido para la estructura de buckets
# class ListaSecuencial:
#     __cant : int
#     __maximo : int
#     __arrego : np.ndarray
#     def __init__(self,maximo : int):
#         self.__maximo = maximo
#         self.__cant = 0
#         self.__arreglo = np.zeros(maximo,dtype=int)
#     def vacia(self):
#         return self.__cant == 0
#     def llena(self):
#         return self.__cant == self.__maximo
#     def insertarPorContenido(self,elemento : int):
#         if not self.llena():
#             repetido = False
#             if not self.vacia():
                
#                 indice = 0
#                 while self.__arreglo[indice]!= 0 and self.__arreglo[indice] != elemento and self.__arreglo[indice] < elemento:
#                     indice += 1
#                 if self.__arreglo[indice] != elemento:
#                     for x in range(self.__cant,indice,-1):
#                         self.__arreglo[x] = self.__arreglo[x-1]
#                     self.__arreglo[indice]= elemento
#                 else:
#                     repetido =True
#             else:
#                 self.__arreglo[0] = elemento   
#             if repetido == False:
#                 self.__cant += 1
#         else:
#             print(f"La lista esta llena el elemento {elemento} no pudo ser insertado")
#     def busquedaBinaria(self,valor : int):
#         izquierda = 0
#         derecha = self.__cant - 1
#         while izquierda <= derecha:
#             medio = (izquierda + derecha)//2
#             valor_medio = self.__arreglo[medio]
#             if valor_medio == valor:
#                 return True
#             elif valor < valor_medio:
#                 derecha = medio - 1
#             else:
#                 izquierda = medio + 1
#         return None


