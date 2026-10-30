matriculas = []
for i in range(5):
    matricula = input("Introduce la matricula: ")
    if matricula in matriculas:
        print("La matricula ya esta registrada")
    else:
        matriculas.append(matricula)

print("Cantidad de alumnos distintos:", len(matriculas))
print(matriculas)