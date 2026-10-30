#creando un diccionario en python
persona={
    "nombre":"Kevin",
    "edad":16,
    "profesion":"ninguno",
    "estudiante":True
}
print(persona)
#accediendo a un valor en especifico
print(persona["edad"])
print(persona["nombre"])
#se puede usar el metodo .get()
#es util porque no da error si la clave no existe
print(persona.get("edad"))
#modificar un valor existente
persona["edad"]=29
print(persona.get("edad"))
#agregar un par clave valor
persona["cuidad"]="ciudad san jose"
print(persona.get("cuidad"))
print(persona)
#recorrer un diccionario con un bucle
for clave, valor in persona.items():
    print(f"{clave}:{valor}")