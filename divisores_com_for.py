a = int(input('coloque um numero inteiro: '))
for x in range(1, a+1):
    if a % x == 0:
        print(x)