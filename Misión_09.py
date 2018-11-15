# Autor: Ithan Alexis Pérez Sánchez
# Matrícula: A01377717
# Descripción: Misión 09 - Listas nuevamente

# El codigo empieza después de esta linea

def extraerPares(listas):

    listaN = []
    for k in listas:
        if k % 2 == 0:
            listaN.append(k)
    return listaN

def extraerMayoresPrevio(listas):

    listaZ = []
    for k in range(1, len(listas)):
        if listas[k] > listas[k-1]:
            listaZ.append(listas[k])
    return listaZ

def intercambiarParejas(listas):

    listaA = []

    for k in range(1, len(listas), 2):
        listaA.append(listas[k])
    for k in range(0, len(listas), 2):
        listaA.append(listas[k])

    return listaA


def intercambiarMM(listas):

        variable = 0

        for k in range(0, len(listas)):
            if listas[k] == max(listas):
                variable = listas[k]
                listas[k] = min(listas)

        for k in range(0, len(listas)):
            if listas[k] == min(listas):
                listas[k] = variable
                break

        return listas

def promediarCentro(listas):

    listas.sort()

    for k in range(0, len(listas)):
        if listas[k] == max(listas):
            listas.remove(max(listas))

    for k in range(0, len(listas)):
        if listas[k] == min(listas):
            listas.remove(min(listas))
            break

    if len(listas) >= 1:
        centro = int(sum(listas) / len(listas))
        return centro
    else:
        if len(listas) == 0:
            return 0

def calcularEstadistica(listas):

    if len(listas) > 0:
        mean = sum(listas) / len(listas)
        deviation = ((sum(listas) - mean) / (len(listas)-1)) ** 0.5
        return mean, deviation
    else:
        if len(listas) >= 1:
            mean = sum(listas) / len(listas)
            deviation = ((sum(listas) - mean) / (len(listas) - 1)) ** 0.5
            return mean, deviation

def calcularSuma(listas):

    if 13 != listas:
        return sum(listas)
    else:
        for k in range(len(listas)):
            if listas[k] == 13:
                if k == 13:
                    listas[k - 1] = 0
                elif k == len(listas) + 1:
                    listas[k + 1] = 0
                    listas[k] = 0

    return sum(listas)


def main():

    lista1 = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    lista2 = [5, 7, 3]
    lista3 = []

    lista4 = [5, 4, 3, 2]

    lista5 = [70, 80, 90]
    lista6 = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
    lista7 = [20, 55, 30, 5, 55, 5]
    lista8 = [5, 9, 1, 8]
    lista9 = [5, 8]

    lista10 = [1, 2, 3, 4, 5, 6]
    lista11 = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]

    lista12 = [1, 2, 3]
    lista13 = [5, 9, 3, 22, 19, 31, 10, 7]

    lista14= [5, 2, 13, 4, 1, 6, 1, 8, 4, 1, 5]

    print("Problema 1. Regresa una lista con los valores pares de la lista original.")
    print("Con la lista", lista1, ", regresa", extraerPares(lista1))
    print("Con la lista", lista2, ", regresa", extraerPares(lista2))
    print("Con la lista", lista3, ", regresa", extraerPares(lista3))

    print("")

    print("Problema 2. Regresa una lista con los valores mayores de la lista original.")
    print("Con la lista", lista1, ", regresa", extraerMayoresPrevio(lista1))
    print("Con la lista", lista4, ", regresa", extraerMayoresPrevio(lista4))
    print("Con la lista", lista3, ", regresa", extraerMayoresPrevio(lista3))

    print("")

    print("Problema 3. Regresa una lista con los intercambiados de la lista original.")
    print("Con la lista", lista1, ", regresa", intercambiarParejas(lista1))
    print("Con la lista", lista12, ", regresa", intercambiarParejas(lista12))
    print("Con la lista", lista3, ", regresa", intercambiarParejas(lista3))

    print("")

    print("Problema 4. Regresa una lista con los valores mayores y menores intercambiados de la lista original.")
    print("Con la lista", lista13, ", regresa", intercambiarMM(lista13))
    print("Con la lista", lista12, ", regresa", intercambiarMM(lista12))
    print("Con la lista", lista3, ", regresa", intercambiarMM(lista3))

    print("")

    print("Problema 5. Regresa una lista con el promedio de la lista original.")
    print("Con la lista", lista5, ", regresa", promediarCentro(lista5))
    print("Con la lista", lista6, ", regresa", promediarCentro(lista6))

    print("Con la lista", lista8, ", regresa", promediarCentro(lista8))
    print("Con la lista", lista9, ", regresa", promediarCentro(lista9))

    print("")

    print("Problema 6. Regresa una lista con los valores de media y desviación estándar de la lista original.")
    print("Con la lista", lista10, ", regresa", calcularEstadistica(lista10))
    print("Con la lista", lista11, ", regresa", calcularEstadistica(lista11))
    print("Con la lista", lista3, ", regresa", calcularEstadistica(lista3))

    print("")

    print("Problema 7. Regresa una lista con los valores de una suma de la lista original.")
    print("Con la lista", lista10, ", regresa", calcularSuma(lista10))
    print("Con la lista", lista14, ", regresa", calcularSuma(lista14))
    print("Con la lista", lista3, ", regresa", calcularSuma(lista3))


main()