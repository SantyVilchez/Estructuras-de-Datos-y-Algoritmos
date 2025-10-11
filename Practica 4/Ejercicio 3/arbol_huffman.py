# ⚠️ ADVERTENCIA:
# Este código implementa Huffman con fines meramente educativos.
# Las funcionalidades están presentes, pero en la práctica real no se logra compresión efectiva.
# El texto codificado se guarda como caracteres '0' y '1' en archivos .txt, lo cual no representa binario real.
# Para una compresión auténtica, deberían utilizarse librerías que traduzcan los códigos a bits y bytes,
# y manejar archivos en modo binario ('wb' / 'rb').
# Aquí se usa texto plano para facilitar la visualización del proceso.
from nodo_arbol import Nodo
from lista_enlazada import ListaEncadenada
class ArbolHuffman:
    __raiz : Nodo
    __dic : dict
    def __init__(self):
        self.__raiz = None
        self.__dic = {}
        self.crear_dict()
        self.estructurador()
    def crear_dict(self):
    # Creo un diccionario siendo las claves todas las letras del archivo
    # y cada valor la frecuencia de aparicion en el archivo de cada letra
    # ejemplo : clave S valor 10 (es decir s aparece 10 veces en el archivo leido)
        with open('texto.txt', mode='r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                for letra in linea.strip().lower():
                    if letra in self.__dic:
                        self.__dic[letra] += 1
                    else:
                        self.__dic[letra] = 1
    def estructurador(self):
    # Creo el arbol huffman donde los nodos mas cercanos a la raiz son aquellos con mayor frecuencia de aparicion
    # es decir este arbol no esta ordenado como un arbol binario
        lista_nodos = ListaEncadenada() #uso una lista enlazada personalizada que elimina por la cabeza y inserta ordenado
        for valor,frecuencia in self.__dic.items():
            lista_nodos.insertar(Nodo(frecuencia,valor)) #aqui recorro todo el diccionario creando una lista de arboles donde cada nodo es un arbol 
        while lista_nodos.cantidad() != 1: # aqui se recorre hasta que en la lista solo quede un nodo que sera el nodo raiz con todos los demas nodos acoplados
            primero = lista_nodos.suprimir() 
            segundo = lista_nodos.suprimir()
            nuevo_valor = primero.getValor() + segundo.getValor()
            nueva_frecuencia = primero.getFrecuencia() + segundo.getFrecuencia()
            nuevo_nodo = Nodo(nueva_frecuencia,nuevo_valor)
            nuevo_nodo.setIzq(primero)
            nuevo_nodo.setDer(segundo)
            lista_nodos.insertar(nuevo_nodo) # insertar ordenado por frecuencia
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

    def cuadro_de_valores(self):
    #devuelve un cuadro con las letras del archivo y su codificacion huffman
        for palabra, frecuencia in self.__dic.items():
            print(f"{'Palabra:':<12} {palabra:<30} | {'Código:':<10} {self.codificador(palabra)}")

    def codificador(self,valor : str):
    # Este metodo recibe una palabra y devuelve su una cadena con el camino hacia esa palabra en el arbol huffman
    # como el arbol no esta ordenado debemos buscar por palabras contenidas, es decir si tal valor esta en tal arbol y asi hasta encontrar el valor que coincida
        raiz = self.__raiz
        camino = ""
        valor = valor.lower()
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
    
    def codificar_archivo_txt(self):
    #Aqui meramente abro un archivo lo recorro codificando cada letra y guardando dicha coficacion en otro archivo llamado archivo codificado 
        archivo_entrada = 'texto.txt'
        archivo_salida = 'texto_codificado.txt'
        with open(archivo_entrada, mode='r', encoding='utf-8') as entrada:
            lineas = entrada.readlines()
        with open(archivo_salida, mode='w', encoding='utf-8') as salida:
            for linea in lineas:
                codificadas = [self.codificador(letra.lower()) for letra in linea.strip()]
                salida.write(' '.join(codificadas) + '\n')

    def decodificador(self, valor : str):
    # Esta funcion recibe una cadena el camino (codificacion) de una palabra y con dichos valores me muevo dentro del arbol para encontrar la palabra que corresponde
        nodo = self.__raiz
        for i in valor:
            if i == "0":
                nodo = nodo.getIzq()
            else:
                nodo = nodo.getDer()
        
        return nodo.getValor()
                        
        
    def decodificar_archivo_txt(self):
    # aqui pues leo un archivo codificado y por cada valor decodifico para recuperar del arbol huffman el valor correspondiente a cada camino (codigo)
        archivo_codificado = 'texto_codificado.txt'
        archivo_salida = 'texto_decodificado.txt'
        with open(archivo_codificado, mode='r', encoding='utf-8') as entrada:
            lineas = entrada.readlines()
        with open(archivo_salida, mode='w', encoding='utf-8') as salida:
            for linea in lineas:
                letras_codificadas = linea.strip().split()
                decodificadas = [self.decodificador(codigo) for codigo in letras_codificadas]
                salida.write(''.join(decodificadas) + '\n')
arbol = ArbolHuffman()
arbol.codificar_archivo_txt()
arbol.decodificar_archivo_txt()