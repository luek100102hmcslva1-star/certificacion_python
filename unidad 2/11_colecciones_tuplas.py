coordenadas=(10.5,20.3,30.2)#Tupla numerica 
nombre=("Luis","Ana","Angel")#TUpla str
for coordenadas in coordenadas:
    print(coordenadas)
for nombre in nombre:
    print(nombre)    
for indice,coordenadas in enumerate(coordenadas):
    print(f"[{indice}]coordenada[{coordenadas}]")    