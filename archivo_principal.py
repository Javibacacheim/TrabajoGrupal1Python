# -- coding: utf-8 --

import paquete_cientifico as p

# x = requests.get('https://www.google.com')
# print(x.text)

print(p.PI)
area = 30
altura = 10
volumen = p.vol_cilindro(altura, area)
print("Volumen de Cilindro: "  + str(volumen))
multiplicacion = p.multiplica(30, 20)
print(multiplicacion)
print(dir(p))
prom = p.promedio(12,34,20)
print("El promedio es :", prom)


if _name_ =="_main_":

    #funciones grupo4
    print(p.calcula_rapidez(10,40))
    print(p.calcula_distancia(60,20))
    print(p.calcula_tiempo(150,80))
    print(p.cel_a_far(33))
    print(p.far_a_cel(110))

    division_final = p.dividir(24,7)
    print("La division es:", division_final)
    resta_final = p.restar(90, 40)
    print("La resta es:", resta_final)
    suma_final = p.sumar(15, 50)
    print("La suma es:", suma_final)
    multiplica_final = p.multiplicar(5,5)
    print("La multiplicacion es:", multiplica_final)


    print(p.promedio(1,2,3))
    print(p.rango(2,2))
    print(p.media_geo(2,2,2))
    print(p.media_armonica(2,2))