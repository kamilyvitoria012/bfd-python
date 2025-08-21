nome = input ('Digite seu nome')
whatsapp = input('Digete seu número do whatsapp')
peso = input('Digite seu peso')
altura = input('Digite sua altura')
peso = float(peso)
altura = float(altura)
agua_ml = peso *35
agua_l =agua_ml / 1000
print(f"{nome} você deve beber {agua_l:.2f} litros de água por dia.")