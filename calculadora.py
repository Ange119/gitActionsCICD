# Creare primero las funciones que va a llevar la calculadora

def sumar (x,y):
    return x + y

def restar (x,y):
    return x - y

def multi (x,y):
    return x * y

def divi (x,y):
    if y == 0:
        return ValueError("No se puede dividir entre cero")
    else:
        return x / y 