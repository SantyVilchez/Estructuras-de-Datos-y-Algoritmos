import numpy as np
from codigos_extra import obtener_primo,ListaEnlazada
class TablaHash:
    __tamaño : int
    __tabla : np.array
    def __init__(self,tamaño : int):
        #El tamaño del arreglo debe ser la cantidad de valor necesario a guardar (m) dividido en 0.7 y dicho numero debe ser primo
        #aqui lo que hago es obtener el entero del tamaño dividido en 0.7 luego redondearlo ya que necesito un numero entero y finalmente
        #envio el valor resultante a la funcion obtener primo que devuelve el valor que envie si es primo o el primo siguiente
        #asi finalmente el tamaño de la tabla es un primo que cumple con las condiciones necesarias
        self.__tamaño = obtener_primo(round(tamaño/0.7))
        #en este ejercicio decidi que era bastante comodo hacer un arreglo numpy de listas enlazadas 
        self.__tabla = np.array([ListaEnlazada() for _ in range(self.__tamaño)], dtype=ListaEnlazada)

    def hash(self,palabra : str):
        #este metodo sirve para trasnformar cadenas en indices
        indice = 0
        base = 31
        for letra in palabra:
            indice = (indice * base + ord(letra)) % self.__tamaño
        return indice
    
    def insertar(self, valor : str):
        #directamente insertamos valor en el indice las colisiones el manejo de colisiones es automatico practicamente jaja
        indice = self.hash(valor)
        self.__tabla[indice].insertar(valor) #los repetidos directamente los maneja el insertar de lista enlazada

    def buscar(self,valor : str):
        indice = self.hash(valor)
        aux = self.__tabla[indice].obtener_cabeza() #obtenemos la cabeza de la lista enlazada en dicha posicion
        encontrado = False
        while aux != None and aux.getElem() != valor: #buscamos entre el valor y las colisiones si es que hubo
            aux = aux.getSig()
        if aux != None:
            encontrado = True 
        return encontrado
    def mostrar(self): #no es un metodo de la funcion misma pero ta buena pal debug
        for i in range(self.__tamaño):
            print(f"[{i}] {self.__tabla[i]}")


