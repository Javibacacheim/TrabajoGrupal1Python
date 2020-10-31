#Funcion suma que recibe dos parámetros

def sumar(a,b):
    suma = a + b
    return suma

suma_final = sumar(15, 50)

print("La suma es:", suma_final)

#Funcion resta con dos parámetros

def restar(a,b):
    resta = a - b
    return resta

resta_final = restar(90, 40)

print("La resta es:", resta_final)

# Funcion division que recibe dos parametros y además valida en caso de recibir un 0 como segundo parametro con if y else

def dividir(a,b):
    if (b!=0):
        division = a/b
        return division
    else: 
        print("No se puede dividir por 0")
  

division_final = dividir(24,7)

print("La division es:", division_final)

#Función que sigue los pasos de una multiplicación con dos parametros

def multiplicar(a,b):
    multiplica = a*b
    return multiplica

multiplica_final = multiplicar(5,5)

print("La multiplicacion es:", multiplica_final)