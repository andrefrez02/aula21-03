a = int(input('Digite um valor para A: '))
b = int(input('Digite um valor para B: '))
c = int(input('Digite um valor para C: '))

if a > b and c > b:
    print(f'{b} é menor do que {a} ou {c}')
else:
    print(f'{a} ou {c} são menores do que {b}')
input()