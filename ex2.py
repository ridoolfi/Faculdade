# Cronometro
# Aluno: Ângelo Marcos
# RA: 23001021

from time import sleep

tmp = int(input('Digite quanto tempo você quer seja cronometrado, em minutos: \n'))
# Transforma os minutos em segundos.
seg = tmp * 60

# Contador e variavel para a edição do texto dos segundos.
contador = 0
tr_seg = 60
window = 1

# Fecha o programa
sair = 'n'

print(f'Cronometrando {tmp} minuto/s')
while sair not in 's':
    for i in range(seg, 0, -1):
        print(f'{tmp - 1} minuto/s e {tr_seg} segundos.')
        contador += 1
        tr_seg -= 1
        if tr_seg == 0:
            tr_seg = 60
        if contador == 60:
            tmp -= 1
            contador = 0
        sleep(1)
    sair = str(input('Sair: s/n')).lower()
    if sair == 'n':
        tmp = int(input('Digite quanto tempo você quer seja cronometrado, em minutos: \n'))
    else:
        print('Valor inválido')
        sair = str(input('Sair: s/n')).lower()
