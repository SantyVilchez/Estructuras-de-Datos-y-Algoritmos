from nodo_lista import Nodo
class lista:
    __cabeza : Nodo
    __cant : int
    __fila_disponible : int
    __columna_disponible : int
    __fila : int
    __columna :int
    def __init__(self,fila : int,columna : int):
        self.__cabeza = None
        self.__cant = 0
        self.__fila = fila
        self.__columna = columna
        self.__fila_disponible = 0
        self.__columna_disponible = 0
    def vacia(self):
        return self.__cant == 0
    def insertar(self,x : int):
        if self.__columna_disponible == self.__columna:
            self.__columna_disponible = 0
            self.__fila_disponible += 1
        nuevo = Nodo(x,self.__fila_disponible,self.__columna_disponible)
        self.__columna_disponible += 1
        if  self.__fila_disponible < self.__fila:
            if self.vacia():
                self.__cabeza = nuevo
            else:
                aux = self.__cabeza
                while aux.getSig()!=None:
                    aux = aux.getSig()
                aux.setSig(nuevo)
            self.__cant+=1
        else:
            print(f"La matriz se lleno no se pudo insertar el valor {x}")
    def recorrer(self):
        aux = self.__cabeza
        while aux  != None:
            print(f"Valor {aux.getValor()} en fila {aux.getFila()} columna {aux.getColumna()}")
            aux = aux.getSig()
    def darCabeza(self):
        return self.__cabeza
def suma(A : lista,B : lista):
    aux_1 = A.darCabeza()
    aux_2 = B.darCabeza()
    while aux_1 != None:
        print(f"valor {aux_1.getValor()+aux_2.getValor()} en fila {aux_1.getFila()} columna {aux_1.getColumna()}")
        aux_1 = aux_1.getSig() 
print("Matriz 1")
matriz_1 = lista(2,2)
matriz_1.insertar(1)
matriz_1.insertar(2)
matriz_1.insertar(3)
matriz_1.insertar(4)
matriz_1.recorrer()
print("Matriz 2")
matriz_2 = lista(2,2)
matriz_2.insertar(1)
matriz_2.insertar(1)
matriz_2.insertar(1)
matriz_2.insertar(1)
matriz_2.recorrer()
print("Suma de Matriz 1 y 2")
suma(matriz_1,matriz_2)