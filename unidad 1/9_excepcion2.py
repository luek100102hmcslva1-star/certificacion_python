try:
    numero1=int(input("ingresa el primer numero"))
    numero2=int(input("ingresa el segundo numero"))
    resultado=numero1/numero2
    print(resultado)
except ZeroDivisionError:
    print("solo introduce numeros")
except ValueError:
    print("division entre cero")
else:
    print("el resultado es:",resultado)
finally:
    print("programa finalizado")            