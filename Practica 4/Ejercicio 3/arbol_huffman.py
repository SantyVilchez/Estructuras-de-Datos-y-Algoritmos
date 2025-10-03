from nodo_arbol import Nodo
from lista_enlazada import ListaEncadenada
import csv
class ArbolHuffman:
    __raiz : Nodo
    __dic : dict
    def __init__(self):
        self.__raiz = None
        self.__dic = {}
        self.crear_dict()
        self.estructurador()
    def crear_dict(self):
        with open('texto.csv', newline='', encoding='utf-8') as archivo:
            filas = csv.reader(archivo)
            for fila in filas:
                for columna in fila:
                    columna = columna.split(' ')
                    for palabra in columna:
                        c = palabra.lower()
                        if c in self.__dic:
                            self.__dic[c] += 1
                        else:
                            self.__dic[c] = 1
    def estructurador(self):
        lista_nodos = ListaEncadenada()
        for valor,frecuencia in self.__dic.items():
            lista29_nodos.insertar(Nodo(frecuencia,valor))
        while lista_nodos.cantidad() != 1:
            primero = lista_nodos.suprimir()
            segundo = lista_nodos.suprimir()
            nuevo_valor = primero.getValor() + segundo.getValor()
            nueva_frecuencia = primero.getFrecuencia() + segundo.getFrecuencia()
            nuevo_nodo = Nodo(nueva_frecuencia,nuevo_valor)
            nuevo_nodo.setIzq(primero)
            nuevo_nodo.setDer(segundo)
            lista_nodos.insertar(nuevo_nodo)
        self.__raiz = lista_nodos.cabeza().getElem()
    def insertar(self, valor :int):
        if not self.__raiz:
            self.__raiz = Nodo(valor)
        else:
            self._insertar(self.__raiz,valor)

    def _insertar(self,nodo : Nodo,valor:int):
        if nodo.getValor() == valor:
            print("El valor ya existe")
        elif valor < nodo.getValor():
            if nodo.getIzq():
                self._insertar(nodo.getIzq(),valor)
            else:
                nodo.setIzq(Nodo(valor))
        else:
            if nodo.getDer():
                self._insertar(nodo.getDer(),valor)
            else:
                nodo.setDer(Nodo(valor))
    def codificador(self,valor : int):
        raiz = self.__raiz
        camino = ""
        if raiz != None:
            nodo_actual = raiz
            while nodo_actual != None and nodo_actual.getValor() != valor:
                if nodo_actual.getIzq() and valor in nodo_actual.getIzq().getValor():
                    camino+="0"
                    nodo_actual = nodo_actual.getIzq()
                else:
                    camino+="1"
                    nodo_actual = nodo_actual.getDer()
        return camino
    def cuadro_decodificador(self):
        with open('texto.csv', newline='', encoding='utf-8') as archivo:
            filas = csv.reader(archivo)
            for fila in filas:
                for columna in fila:
                    columna = columna.split(' ')
                    for palabra in columna:
                        print(f"Palabra: {palabra}\ncodigo: {self.codificador(palabra)}")
    def codificador_archivo(self):
        with open('texto.csv','r') as archivo_entrada:
            with open('texto_codificado.csv', 'w') as archivo_salida:
                lector = csv.reader(archivo_entrada)
                escritor = csv.writer(archivo_salida)
                for fila in lector:
                    for renglon in fila:
                        renglon = renglon.split(" ")
                        nueva_fila = [self.codificador(palabra) for palabra in renglon]
                        escritor.writerow(nueva_fila)
    def decodificador(self, valor : str):
        nodo = self.__raiz
        for i in valor:
            if i == "0":
                nodo = nodo.getIzq()
            else:
                nodo = nodo.getDer()
        return nodo.getValor()
                        
        
    def decodificador_archivo(self):
        with open('texto_codificado.csv','r') as archivo_entrada:
            with open('texto_decodificado.csv', 'w') as archivo_salida:
                lector = csv.reader(archivo_entrada)
                escritor = csv.writer(archivo_salida)
                for fila in lector:
                    for renglon in fila:
                        nueva_fila = [self.decodificador(palabra) for palabra in renglon]
                        escritor.writerow(nueva_fila)
                        
    def Raiz(self):
        return self.__raiz
arbol = ArbolHuffman()
arbol.cuadro_decodificador()
print(arbol.codificador("minuto"))
print(arbol.decodificador("0001101"))