import math
import random 

def anagrama(cadena, lista, n):
    largo = len(cadena)
    if (n == 3 or largo == 1 or largo == 0):
        return lista
    for i in range(0, largo):
        for j in range(0, largo):
            enlistada = list(cadena)
            neu = list(cadena)
            aux = neu[i]
            neu[i] = enlistada[j]
            neu[j] = aux
            neu_str = neu
            if neu_str not in lista:
                lista.append(neu_str)
                print(i, "/", j, "soluciones encontradas")     
        anagrama(lista[-1], lista, n +1)    
    return lista

#complejidad imposible
def anagrama_random(cadena, lista):
    largo = len(cadena)
    limite = math.factorial(largo)
    i = 0
    while i < limite:
        enlistado = list(cadena)
        random.shuffle(enlistado)
        if enlistado not in lista:
            lista.append(enlistado)
            i += 1
            if i % 2 == 0:
                print(i, "/", limite, "soluciones encontradas")
    return lista
        


def __main__():
    cadena = "conchudo"
    lista = []
    lista = anagrama(cadena, lista, 0)
    
    for i in lista:
        print(i)
    print("se encontraron", len(lista), "anagramas.")
__main__()