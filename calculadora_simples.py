while True:
    a = float(input('insira o primeiro numero: '))
    b = float(input('insira o segundo numero: '))
    resultado = 0
    print('''Qual é a operação que deseja?
          +
          -
          *
          /
          ''')
    resposta = input()
    while not (resposta == '+' or resposta == '-' or resposta == '*' or resposta == '/'):
    #while resposta != '+' and resposta != '-' and resposta != '*' and resposta != '/'
        print('operador inavilo, tente novamente')
        resposta = input('')
    if resposta == '+':
        resultado += a + b
    elif resposta == '-':
        resultado += a - b
    elif resposta == '*':
        resultado += a * b
    elif resposta == '/':
        resultado += a / b
    print(resultado)
    saida = input('Digite "exit" para sair ou qualquer coisa para continuar')
    if saida == 'exit':
        break