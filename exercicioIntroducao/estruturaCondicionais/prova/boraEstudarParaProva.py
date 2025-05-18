x = int(input('Digite o valor de x(1, 2 ou 3): '))
num1 = int(input('Digite um primeiro numero: '))
num2 = int(input('Digite um segundo numero: '))
num3 = int(input('Digite um terceiro numero: '))

if x == 1:
    if num1 <= num2 <= num3:
        print(num1, num2, num3)
    
    elif num1 <= num3 <= num2:
        print(num1, num3, num2)

    elif num2 <= num3 <= num1:
        print(num1, num3, num2)

    elif num2 <= num1 <= num3:
        print(num2, num1, num3)

    elif num3 <= num1 <= num2:
        print(num3, num1, num2)

    elif num3 <= num2 <= num1:
        print(num3, num2, num1)
    else: 
        print('invalido')

elif x == 2:
    if num1 >= num2 >= num3:
        print(num1, num2, num3)
    
    elif num1 >= num3 >= num2:
        print(num1, num3, num2)

    elif num2 >= num3 >= num1:
        print(num1, num3, num2)

    elif num2 >= num1 >= num3:
        print(num2, num1, num3)

    elif num3 >= num1 >= num2:
        print(num3, num1, num2)

    elif num3 >= num2 >= num1:
        print(num3, num2, num1)
    else: 
        print('invalido')

elif x == 3:
    if num1 <= num2 >= num3:
        print(num1, num2, num3)
    
    elif num3 <= num2 >= num1:
        print(num3, num2, num1)

    elif num1 <= num3 >= num2:
        print(num1, num3, num2)

    elif num2 <= num3 >= num1:
        print(num1, num3, num1)

    elif num2 <= num1 >= num3:
        print(num2, num1, num3)

    elif num3 <= num1 >= num2:
        print(num3, num1, num2)
    else: 
        print('invalido')