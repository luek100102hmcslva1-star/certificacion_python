cadena1='hola'
cadena2="mundo"
multilinea="""Esto es una cadena
de varias lineas"""
print(cadena1 + cadena2 + multilinea)
#cadena y repeticion
eco="ja"*3
print(eco)
tu_nombre='Kevin'
print(tu_nombre.upper())
#cambiar ua  cadena de mayusculas a minusculas
print(tu_nombre.lower())
#remplazar texto en una cadena 
frase="Me gusta programacion"
print(frase.replace("programacion","recreo"))
#formato de concatenar cadenas con  valores (F-string)
edad='16'                
nombre='Kevin'
mensaje=f"hola me llamo {nombre} y tengo\n {edad}años"
print(mensaje)
#contar los caracteres de una cadena 
texto= "¡Felicidades por aun continuar en el CECY!!!"
cantidad_caracteres=len(texto)
print(cantidad_caracteres)
oracion="Aprender python es divertido"
if "python" in oracion:
    print("Encontrado")
else:
    print("no esta")
ncadena="oooo"
print(ncadena.isalpha())
print(ncadena.isdigit())        