

LETRAS = [
    "T","R","W","A","G",
    "M","Y","F","P","D",
    "X","B","N","J","Z",
    "S","Q","V","H","L",
    "C","K","E",    
]

def calculadora_dni(numero_dni):
    resto_div = numero_dni % len(LETRAS)
    
    return LETRAS[resto_div]
