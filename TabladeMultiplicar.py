#Tabla de Multiplicar con funciones


def calculo ():#Creamos una funcion que en su interior tendra el calculo de las tablas de multiplicar
    
    for i in range(1,11):#establece la secuencia de numero para la tabla
        for numero in range(1,11):#establece el numero representantivo de la tabla
            if i == numero:#validamos si el numero secuencial es igual al numero de tabla a representar
                print(f"""
                Tabla del {numero}
                """)
                for j in range(1,11):#en caso de ser cierto procesamos la tabla
                    res = j * numero #ejecutamos la operacion matematica
                    print(f"{j} x {numero} = {res}")#escribimos en pantalla el resultado 

calculo()#Ejecutamos la llamada a la funcion






    




        

