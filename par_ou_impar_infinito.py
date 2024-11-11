while True:
    x = int(input('Insira um número: '))
    if x % 2 == 0:
        print(f'O numero {x} é par')
    else:
        print(f'O numero {x} é impar')
    op = input('Digite "exit" para sair ou qualquer outra coisa para continuar: ')
    if op == 'exit':
        break
print('Até mais!')