#[A,B,C,D]
matriz = [
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'],  
    ['n',  'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']   
]

for i in range(0,2):
    for j in range(0,13):
        print(f"posicion[{i}][{j}]={matriz[i][j]}")

