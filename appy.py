# app.py

import matematica

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

try:
    print("Soma:", matematica.somar(num1, num2))
    print("Subtração:", matematica.subtrair(num1, num2))
    print("Multiplicação:", matematica.multiplicar(num1, num2))
    print("Divisão:", matematica.dividir(num1, num2))
except ValueError as e:
    print("Erro:", e)
