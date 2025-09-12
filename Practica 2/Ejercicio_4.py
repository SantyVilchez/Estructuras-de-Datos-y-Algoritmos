from Ejercicio_1 import PilaEncadenada
pila_1 = PilaEncadenada()
pila_2 = PilaEncadenada()
pila_3 =PilaEncadenada()
pilas = [pila_1,pila_2,pila_3]
def InterfazGrafica(pilas):
    for x in range(3):
        print(f"Pila {x+1}")
        pilas[x].grafico()
        
def JuegoDeHanoi(n,lista:list[PilaEncadenada],c=0):
    for x in range(n,0,-1):
        lista[0].insertar(x)
    while  lista[2].cantidad() != 4 or lista[2].tope() !=1:
        InterfazGrafica(lista)
        origen = int(input("Ingrese Pila Origen: "))
        destino = int(input("Ingrese Pila Destino: "))
        if (lista[origen-1].tope() if not lista[origen-1].vacia() else n+1) < (lista[destino-1].tope() if not lista[destino-1].vacia() else n + 1):
            print(f"---------------Se Movio el elemento {lista[origen-1].tope()} de la Pila {origen} a la Pila {destino} -------------")
            lista[destino-1].insertar(lista[origen-1].suprimir())
            c+=1
        else:
            print("---------------Movimiento Invalido-------------")
    InterfazGrafica(lista)
    print(F"Felicidades Ganaste con {c} de {2**n-1}")
JuegoDeHanoi(4,pilas)