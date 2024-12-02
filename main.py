'''Ej1. Media de Notas
Crea una función llamada calcular_media que reciba un número variable de
calificaciones y calcule la media aritmética de las mismas. La función debe
comportarse de la siguiente manera:

Si no se pasan calificaciones, debe retornar el mensaje: "No se proporcionaron
notas para calcular la media."
Si se proporcionan notas, debe:

• Calcular la media aritmética sumando todas las notas y dividiendo entre
el número total.

• Retornar la media con dos decimales.
'''

def media_nota(*notas:float)-> float:
    media=0

    for num in notas:
        media+=num

    media= media/len(notas)
    return media

print(media_nota(8,1,6,9,10,10))

'''Ej 2. Calculadora Multiuso

Escribe una función llamada calculadora_multiuso que reciba:
• Un argumento obligatorio llamado operacion (puede ser "suma", "resta",
"multiplicación", o "división").

• Un número variable de argumentos (*args) que representen los números
sobre los que se realizará la operación.

• Un argumento opcional mostrar_paso_a_paso que por defecto sea
False.

La función debe:
Realizar la operación indicada sobre todos los números de *args.

• Suma: sumar todos los números.

• Resta: restar los números en el orden en que se reciben.

• Multiplicación: multiplicar todos los números.

• División: dividir los números en el orden en que se reciben.

Si el argumento mostrar_paso_a_paso es True, imprimir los pasos de la
operación.

Python
Restricciones:
• Si no se proporcionan números en *args, la función debe retornar un
mensaje de error: "Debe proporcionar al menos un número para operar."
• Si operación no es válida, debe retornar un mensaje de error:
"Operación no reconocida. Use suma, resta, multiplicación o división."'''

def calculadora_multiuso(operacion:str,*num:float,mostrar_paso_a_paso:bool=False):
    resultado:float=0
    if mostrar_paso_a_paso==True:

        if operacion == "suma":
            for numeros in num:
                print(resultado, "+", numeros, "=", resultado+numeros)
                resultado+=numeros

        elif operacion == "resta":
                for numeros in num:
                    print(resultado, "-", numeros, "=", resultado-numeros)
                    resultado-=numeros

        elif operacion == "multiplicacion":
            resultado = num[0]
            for numeros in num:
                print(resultado, "*", numeros, "=", resultado*numeros)
                resultado*=numeros

        elif operacion == "division":
            resultado = num[0]
            for numeros in num:
                if numeros==0:
                    return "Sintax Error"
                print(resultado, "/", numeros, "=", resultado/numeros)
                resultado/=numeros
    else:
        if operacion == "suma":
            for numeros in num:
                resultado += numeros
        elif operacion == "resta":
            for numeros in num:
                resultado -= numeros
        elif operacion == "multiplicacion":
            resultado = 1
            for numeros in num:

                resultado *= numeros
        elif operacion == "division":
            resultado = 1
            for numeros in num:
                if numeros==0:
                    return "Sintax Error"

                resultado /=numeros
    return resultado

print(calculadora_multiuso("division",0,3,5,6,7,7,7, mostrar_paso_a_paso= True))