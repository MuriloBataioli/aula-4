a = int(input('coloque um numero inteiro: '))
for x in range(2, a):
    if a % x == 0:
        print(f'{a} não é primo')
        exit()
print(f'{a} é primo')