# Calculadora

sis = 's'   # Mantém o sistema em loop.

# Váriaveis necessárias

soma = 0
calc_som = 0

# Chama a funcao que determina o tipo de calculo
while sis == 's':
    opc = str(input('''Que tipo de calculo você quer fazer?
    A - Para Adição
    S - Para subtração
    D - Para divisão
    M - Para multiplicação

    Digite a opção desejada:\n''')).lower()   # Informa as opções para o user escolher
    if opc == 'a':
        num = int(input('Quantos números você deseja somar?\n'))
        for i in range(0, num):
            if calc_som < 1:
                numeros = int(input('Informe o primeiro número: '))
            else:
                numeros = int(input('Informe mais um número: '))
            calc_som += numeros
        print(f'O resultado da soma dos {num} números é igual a {calc_som}')

    elif opc == 's':
        s1 = float(input('Informe o primeiro número:'))
        s2 = float(input('Informe o segundo número:'))
        print(f'{s1} - {s2} = {s1 - s2}')
    
    elif opc == 'd':
        d1 = float(input('Informe o primeiro número:'))
        d2 = float(input('Informe o segundo número:'))
        print(f'{d1} / {d2} = {d1 / d2}')
    elif opc == 'm':
        m1 = float(input('Informe o primeiro número:'))
        m2 = float(input('Informe o segundo número:'))
        print(f'{m1} * {m2} = {m1 * m2}')
    else:
        print('Opção inválida')
    sis = str(input('Você deseja continuar S/N?\n')).lower()
