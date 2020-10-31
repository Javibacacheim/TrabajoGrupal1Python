#Área y perímetro Circulo

#Ingrese radio

def area_circulo(r):
    area_circ = 3.14 * r**2
    return (area_circ)

def perimetro_circulo(r):
    per_circ = 2 * 3.14 * r
    return (per_circ)

#Área y perímetro triángulo

#Ingresar base (b) y altura (h)

def area_triangulo(b,h):
    area_triang = (b * h ) / 2
    return (area_triang)

def perimetro_triangulo(b):
    per_triang = 3 * b
    return (per_triang)

#Área y perímetro rectángulo

#Ingresar ancho (a) y largo (l)

def area_rectangulo(b,l):
    area_rect = (b * l)
    return (area_rect)

def perimetro_rectangulo(a,b):
    per_rect = 2 * (a + b)
    return (per_rect)

#Distancia recorrida, dado tiempo (t) y velocidad (v)


def dist_recorrida(vel,tiempo):
    distancia = vel * tiempo
    return (distancia)

if __name__ == "__main__":
    print(area_circulo(2))
    print(perimetro_circulo(2))
    print(area_triangulo(2,5))
    print(perimetro_triangulo(5))
    print(area_rectangulo(3,5))
    print(perimetro_rectangulo(3,5))
    print(dist_recorrida(2,2))