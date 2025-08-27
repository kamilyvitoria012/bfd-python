

def calcular_media(nota1, nota2):
  media = (nota1 + nota2)/2
  return media
nome = input('Digite seu nome:')
nota1 = float (input('Digite sua nota1'))
nota2 =float (input('Digite a sua nota2:'))

media = calcular_media(nota1, nota2)

# Verifica situação
if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print(f'Aluno: {nome}')
print(f'Média: {media}')
print(f'Situação: {situacao}')