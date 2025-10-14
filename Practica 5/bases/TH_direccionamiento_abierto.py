import numpy as np
from codigos_extra import obtener_primo
class TablaHash:
    __tamaño : int
    __tabla : np.array
    def __init__(self,tamaño : int):
        #El tamaño del arreglo debe ser la cantidad de valor necesario a guardar (m) dividido en 0.7 y dicho numero debe ser primo
        #aqui lo que hago es obtener el entero del tamaño dividido en 0.7 luego redondearlo ya que necesito un numero entero y finalmente
        #envio el valor resultante a la funcion obtener primo que devuelve el valor que envie si es primo o el primo siguiente
        #asi finalmente el tamaño de la tabla es un primo que cumple con las condiciones necesarias
        self.__tamaño = obtener_primo(round(tamaño/0.7))
        self.__tabla = np.full(self.__tamaño,None,dtype = object)
    
    def hashing(self, valor:int):
        #Metodo de transformacion hay varios, este especificamente solo funciona para enteros
        return valor % self.__tamaño
    
    def insertar(self, valor:int):
        indice = self.hashing(valor)
        repetido = False #En tablas hash no se insertan valores repetidos

        if self.__tabla[indice] == None: #Si en la posicion del valor hasheado esta libre se inserta
            self.__tabla[indice] = valor
        elif self.__tabla[indice] == valor: #si en la posicion del valor hasheado esta otro valor igual  no se inserta
            repetido = True
        else: #Hubo una colisicion guardamos en una variable final el indice en el que estabamos esto nos servira para saber que reccorimos toda la tabla
            final = indice
            indice = (indice + 1) % self.__tamaño # aqui nos movemos a la siguiente posicion, el % self.__tamaño hara que el recorrido sea circular es decir posamos recorrer toda la tabla, si! como en cola circular XD
            while self.__tabla[indice] != None and indice != final:
                if self.__tabla[indice] == valor:
                    repetido = True
                indice = (indice + 1) % self.__tamaño
            if repetido is False: #si el valor se repite no se inserta nada
                if indice != final:# si el indice es igual al final quiere decir que se recorrio todo el arreglo y no se encontro posicion valida, osea que si son distintos se encontro lugar disponible
                    self.__tabla[indice] = valor
        if repetido is True:
            print("Valor no insertador por esta ya en la lista")
    def buscar(self, valor : int):
        indice = self.hashing(valor)
        encontrado = False
        if self.__tabla[indice] == valor: # si el valor de la posicion encontrada con hash es igual al valor se encontro el valor, no hubo colisiones
            encontrado = True
        else: #sino es que hubo colisiones :c
            fin = indice
            indice = (indice + 1) % self.__tamaño  #nos permite hacer la busqueda circular
            while self.__tabla[indice] != valor and indice != fin:
                indice = (indice + 1) % self.__tamaño
            if indice != fin:
                encontrado = True
        return encontrado
 