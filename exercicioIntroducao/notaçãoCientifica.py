numero = float(input('Digite um número: '))

if numero == 0:
    print('0 X 10^0')
else:
    expoente = 0
    mantissa = numero

    while abs(mantissa) >= 10:
        mantissa /= 10
        expoente += 1

    while abs(mantissa) < 1:
        mantissa *= 10
        expoente -= 1

    print(f'{mantissa:.2f} x 10^{expoente}')