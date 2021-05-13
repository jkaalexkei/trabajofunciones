
print("Trabajo con Funciones")

valor = input("introduzca el numero de valores a sumar: ")#capturamos el numero de valores a sumar

def valoresSumar(dato): #creamos una funcion que recibe como argumento eñ numero de valores a sumar

    contador = 1 #creamos un contador

    res = 0 #esta variable almacenara el resultado de la suma
    
    while contador <= int(dato):#creamos un bucle para recorrer la cantidad de valores a sumar

        numero = int(input("Ingrese Valor: "))#capturamos los valores que se sumaran

        res = res + numero# realizamos la suma de los valoresa

        contador += 1 #incrementamos el contador hasta que se cumpla la condicion
    #kjk
    
    print("El resultado es: " + str(res)) #imprimimos por pantalla el resultado de la suma

valoresSumar(int(valor))#ejecutamos la llamada a la funcion


