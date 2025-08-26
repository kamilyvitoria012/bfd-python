# Função número primo
def eh_primo(numero):
    if numero < 2:
        return False 
    for i in range(2, numero):
        if numero % i == 0:
            return False  
    return True  

n = int(input("Digite um número: "))
if eh_primo(n):
    print(f"{n} é primo!")
else:
    print(f"{n} não é primo.")
