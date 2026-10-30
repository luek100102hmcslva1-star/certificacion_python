#el mapa del tesoro
mapa=[
    [".",".",".",".",],
    [".",".","A",".",],
    [".",".",".",".",],
    [".","B",".",".",],   
]
filas=len(mapa)
columnas=len(mapa[0])
#recorriendo la matriz con ciclso anidados 
#ciclo externo para manejar filas(i)
for i in range(filas):
    #ciclo externo para el manejo de columnas(j)
    for j in range(columnas):
        #verificamos si encontramos el tesoro 
        if mapa[i][j]=="A":
            print(f"Tesoro encontrado en la posicion [{i}][{j}]")
        if mapa[i][j]=="B":
                    print(f"Tesoro encontrado en la posicion [{i}][{j}]")
                   