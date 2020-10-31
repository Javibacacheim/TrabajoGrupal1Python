#Formula que calcula la rapidez de un objeto en base a la distancia recorrida y el tiempo ocupado
def calcula_rapidez(distancia, tiempo):
    rapidez = distancia/tiempo
    return rapidez

#Formula que calcula la la distancia recorrida de un objeto en base al tiempo utilizado y su velocidad
def calcula_distancia(tiempo, rapidez):
    distancia = tiempo*rapidez
    return distancia

#Formula que calcula el tiempo que tarda un objeto en recorrer cierta distancia
def calcula_tiempo(distancia, rapidez):
    tiempo = distancia/rapidez
    return tiempo

#Formula que convierte de grados Celsius a Farenheit
def cel_a_far(celsius):
    resultado = celsius*1.8+32
    return "Grados Celsius ingresados:",celsius," Grados Farenheit :",resultado

#Formula que convierte de grados Farenheit a Celsius
def far_a_cel(fare):
    resultado = (fare-32)/1.8
    return "Grados Farenheit ingresados:",fare," corresponde en Celsius :",resultado



if __name__ =="__main__":
    print(calcula_rapidez(10,40))
    print(calcula_distancia(60,20))
    print(calcula_tiempo(150,80))
    print(cel_a_far(33))
    print(far_a_cel(110))