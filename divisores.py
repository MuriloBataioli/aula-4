a = int(input('coloque um numero inteiro: '))
x = 1
while x <= a:
    if a % x == 0:
        print(x)
    x += 1