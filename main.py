from calculadora_dni import calculadora_dni

numero_dni = int (input("introduce el numero del DNI:"))


letra_dni = calculadora_dni(numero_dni)
print(f"DNI CALCULADO: {numero_dni}-{letra_dni}")
