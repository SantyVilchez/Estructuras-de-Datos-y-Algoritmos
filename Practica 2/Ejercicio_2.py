
from Ejercicio_1 import PilaEncadenada,PilaSecuencial
pila = PilaEncadenada()
pilaSecuencial = PilaSecuencial(30)
def transmutadorBinarioEncadenado(n,pila:PilaEncadenada):
    while n > 2:
        pila.insertar(n % 2)
        n = n//2
    pila.insertar(n%2)
    while pila.vacia() != True:
        print(pila.suprimir())


print("Pila Encadenada")
transmutadorBinarioEncadenado(25,pila)
