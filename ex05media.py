nota1 = float(input('Digite o valor da primeira nota: '))
nota2 = float(input('Digite o valor da segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 6:
    print(f'APROVADO!\nVocê foi aprovado com uma média de {media}')
else:
    print(f'REPROVADO!\nVocê foi reprovado com uma média de {media}')