from lista_de_canciones import ListaEncadenada
def menu():
    op=int(input("""
                 Menu de Opciones
    [0] Salir
    [1] Agregar Cancion al final de la lista
    [2] Insertar por posicion
    [3] Buscar por posicion     
    [4] Dada una cancion dar posicion
    [5] Suprimir por posicion
    [6] Mostrar Canciones                                
    --->"""))
    return op
if __name__ == '__main__':
    GL = ListaEncadenada()
    opcion = menu()
    while opcion!=0:
        if(opcion==1):
           GL.inciso_1()
        elif(opcion==2):
            GL.inciso_2()
        elif(opcion==3):
            GL.inciso_3()
        elif(opcion==4):
            GL.inciso_4()
        elif(opcion==5):
            GL.inciso_5()
        elif(opcion==6):
            GL.recorrer()
        else:
            print("Opcion invalida")
        opcion=menu()

"""
1
Baby Shark
1
Badbuny Baby
1
El meneito
1
Marama
1
El laumento
"""