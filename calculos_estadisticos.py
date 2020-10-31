#Cálculo Promedio 3 números

def promedio(a,b,c):
    prom = (a + b + c) / 3
    return (prom)

#Cálculo de Rango

def rango(a,b):
    rank = b - a
    return (rank)
 
#Media Geométrica

def media_geo(a,b,c):
    mean_geo = (a*b*c)**(1/3)
    return (mean_geo)

#Media Armónica

def media_armonica(a,b):
    mean_arm =( 2 / ((1/a) + (1/b)))
    return (media_armonica)
 
 

if __name__ == "__main__":
    print(promedio(1,2,3))
    print(rango(2,2))
    print(media_geo(2,2,2))
    print(media_armonica(2,2))