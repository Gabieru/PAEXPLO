from random import randint
def adivinar_par_o_impar():
    """
    Esta función representa el juego de adivinar si un número es par o impar.
    Tienes que permitir que el usuario ingrese una de las dos opciones y
    generar un número aleatorio para ver si es par o impar.
    Se debe mostrar si el usuario adivina correctamente o no.
    """
    while True:
        input("Presiona enter para continuar")
        ingreso = input("INGRESA PAR O IMPAR (Recuerda ingresarlo textual (PAR) o (IMPAR)): ")
        print(ingreso)
        generado = int(randint(1,2))
        print(generado)
        if ingreso == "PAR":
            ingreso = 1
        elif ingreso == "IMPAR":
            ingreso = 2
        if ingreso 
        else:
            print("ta malo")
            print(f"El numero era {numero_generado}")
        continuar = int(input("Ingresa 1 para seguir jugando, 2 para salir: "))
        if continuar == 1:
            pass
        elif continuar == 2:
            break