num = int(input('Digite um número inteiro: '))

if num <= 0:
    print(f'DIGITE UM VALOR POSITIVO E MAIOR DO QUE 0')
else:
    raiz = num ** 0.5
    print(f'A raíz de {num} é {raiz:.2f}.')