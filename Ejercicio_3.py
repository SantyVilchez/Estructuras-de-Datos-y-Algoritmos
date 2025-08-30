from random import random
from Ejercicio_1 import PilaEncadenada
pila = PilaEncadenada()
def PromedioEscalera(n,pila:PilaEncadenada):
    while n > 0:
        if n > 1 and random() > 0.5:
            pila.insertar(2)
            n-=2
        else:
            pila.insertar(1)
            n-=1
    while not pila.vacia():
        print(pila.suprimir())
PromedioEscalera(7,pila)