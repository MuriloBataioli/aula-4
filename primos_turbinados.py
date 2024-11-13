a = int(input('coloque um numero inteiro: '))
x = 2

while x < a:
    if a % x == 0:
        print(f'{a} não é primo')
        exit()
    x += 1
print(f'{a} é primo')