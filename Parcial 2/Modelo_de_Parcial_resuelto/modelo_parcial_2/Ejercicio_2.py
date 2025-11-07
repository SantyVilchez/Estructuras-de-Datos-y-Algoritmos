#A
class TablaHash:
    __tamaño : int
    __tabla : np.array
    #como las colisiones esperadas no las especifican me las saco de los webos
    def __init__(self,claves_a_almacenar = 1000, colisiones_esperadas = 5):
        self.__tamaño = obtener_primo(round(claves_a_almacenar/colisiones_esperadas))
        self.__tabla = np.array(self.__tamaño, dtype=ListaEnlazada)
        for i in range(self.__tamaño):
            self.__tabla[i]= ListaEnlazada()
#B
    def hash(self,valor : int):
        return valor % self.__tamaño
#C
    def buscar(self,valor):
        indice = self.hash(valor)
        colisiones = 0
        encontrado = False
        aux = self.__tabla[indice].obtenerCabeza()
        while aux != None and aux.getDato() != valor:
            aux = aux.getSig()
            colisiones +=1
        if aux != None:
            print(colisiones)
            encontrado = True
        return encontrado

    
        