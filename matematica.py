# matematica.py

#somar dois números
def somar(a, b):
    return a + b

#subtrair dois números
def subtrair(a, b):
    return a - b

#multiplicar dois números
def multiplicar(a, b):
    return a * b

#dividir dois números
def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero")
    return a / b
