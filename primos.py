a = int(input('coloque um numero inteiro: '))
x = 1
count = 0
while x <= a:
    if a % x == 0:
        print(x)
        count += 1
    x += 1
if count == 2:
    print(f'{a} é primo')
else:
    print(f'{a} não é primo')