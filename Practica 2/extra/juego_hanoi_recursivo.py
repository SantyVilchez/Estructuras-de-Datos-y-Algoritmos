
def InterfazGrafica(matriz):
    cols = matriz
    max_rows = max((len(c) for c in cols), default=0)
    COLW = 8
    SEP = "   "
    for i in range(max_rows - 1, -1, -1):
        partes = []
        for col in cols:
            if i < len(col):
                s = "-" * (2 * col[i])
            else:
                s = ""
            s = f"{s:^{COLW}}"
            mid = COLW // 2
            s = s[:mid] + s[mid+1:]
            partes.append(s)
        print(SEP.join(partes))

pilas = [[4,3,2,1],[],[]]

def JuegoDeHanoi(pilas:list,movimientos):
    if pilas[2] != [4,3,2,1]:
        InterfazGrafica(pilas)
        print(pilas)
        origen = int(input("Ingrese Pila Origen "))
        destino = int(input("Ingrese Pila Destino "))
        if  (pilas[origen-1][-1] if pilas[origen-1] else 5) < (pilas[destino-1][-1] if pilas[destino-1] else 5):
            pilas[destino-1].append(pilas[origen-1].pop())
            JuegoDeHanoi(pilas,movimientos+1)
        else:
            print("Movimiento Invalido")
            JuegoDeHanoi(pilas,movimientos)
    else:
        InterfazGrafica(pilas)
        print(f"Ganaste Felicidades con {movimientos} movimientos posibles de {(2**4)-1} movimientos")

JuegoDeHanoi(pilas,0)

