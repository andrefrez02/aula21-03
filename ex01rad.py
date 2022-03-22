import math

a = float(input('Digite o ângulo em graus: '))
sombra = float(input('Digite o comprimento da sombra em metros: '))

a = math.radians(a)
h = sombra * math.tan(a)

print(f'A altura do prédio é: {h:.2f} metros')