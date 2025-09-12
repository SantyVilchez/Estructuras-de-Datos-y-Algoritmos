from random import random
from Ejercicio_5 import ColaEncadenada
cola = ColaEncadenada()
def PromedioEscalera(n,cola : ColaEncadenada):
    while n > 0:
        if n > 1 and random() > 0.5:
            cola.insertar(2)
            n-=2
        else:
            cola.insertar(1)
            n-=1
    cola.recorrer()
PromedioEscalera(7,cola)
#Las salidas estas en orden invertido respecto a la pila