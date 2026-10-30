alumno = []
promedio = []

cantidad = int(input("¿cuantos alumnos deseas ingresar"))

for contador in range(cantidad):
    nombre_alumno = input(f"nombre del alumno{contador+1}")
    calificacion = float(input(f"el promedio de{nombre_alumno}"))
    alumno.append(nombre_alumno)
    promedio.append(calificacion)

promedio_bajo = promedio[0]
for calificacion in promedio:
    if calificacion < promedio_bajo:
        promedio_bajo = calificacion

promedio_alto = promedio[0]
for calificacion in promedio:
    if calificacion > promedio_alto:
        promedio_alto = calificacion
print("\nPromedio mas alto:", nombre_alumno, promedio_alto)
print("Promedio mas bajo:", nombre_alumno, promedio_bajo)


