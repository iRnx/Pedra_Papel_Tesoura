from random import randint
from time import sleep


def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mERRO ! Digite um número inteiro válido.\033[m')
        if ok:
            break

    return valor


def simnao(msg):
        n = str(input(msg)).strip().upper()[0]
        if n not in "SN":
            while n not in "SN":
                n = str(input(msg)).strip().upper()[0]
        if n.isnumeric():
            while n.isnumeric():
                n = str(input(msg)).strip().upper()[0]
        if n == 'N':
            exit()


if __name__ == '__main__':
    pontos_jogador = 0
    pontos_pc = 0
    empates = 0
    while True:
        itens = ('Pedra', 'Papel', 'Tesoura')
        computador = randint(0, 2)
        print('''Escolha uma opção:   
        [ 0 ] Pedra
        [ 1 ] Papel
        [ 2 ] Tesoura''')
        jogador = leiaint('qual é sua jogada bro ? ')
        if jogador > 2 or jogador < 0:
            while jogador > 2 or jogador < 0:
                jogador = leiaint('qual é sua jogada bro ? ')

        print(f'Computador jogou: {itens[computador]}')
        print(f'Jogador jogou: {itens[jogador]}\n')
        sleep(1.5)

        if computador == 0:
            if jogador == 0:
                print('EMPATE')
                empates += 1
                print(f'{"HUMANO":<8} {"MAQUINA":<8}  {"EMPATE":<8}')
                for c in pontos_jogador, pontos_pc, empates:
                    print(end=f'{c:<11}')

            elif jogador == 1:
                print('JOGADOR VENCE')
                pontos_jogador += 1
                print(f'{"HUMANO":<8} {"MAQUINA":<8}  {"EMPATE":<8}')
                for c in pontos_jogador, pontos_pc, empates:
                    print(end=f'{c:<11}')

            elif jogador == 2:
                print('COMPUTADOR VENCE')
                pontos_pc += 1
                print(f'{"HUMANO":<8} {"MAQUINA":<8}  {"EMPATE":<8}')
                for c in pontos_jogador, pontos_pc, empates:
                    print(end=f'{c:<11}')

        if computador == 1:
            if jogador == 0:
                print('COMPUTADOR VENCE')
                pontos_pc += 1
                print(f'{"HUMANO":<8} {"MAQUINA":<8}  {"EMPATE":<8}')
                for c in pontos_jogador, pontos_pc, empates:
                    print(end=f'{c:<11}')

            elif jogador == 1:
                print('EMPATE')
                empates += 1
                print(f'{"HUMANO":<8} {"MAQUINA":<8}  {"EMPATE":<8}')
                for c in pontos_jogador, pontos_pc, empates:
                    print(end=f'{c:<11}')

            elif jogador == 2:
                print('JOGADOR VENCE')
                pontos_jogador += 1
                print(f'{"HUMANO":<8} {"MAQUINA":<8}  {"EMPATE":<8}')
                for c in pontos_jogador, pontos_pc, empates:
                    print(end=f'{c:<11}')

        if computador == 2:
            if jogador == 0:
                print('JOGADOR VENCE')
                pontos_jogador += 1
                print(f'{"HUMANO":<8} {"MAQUINA":<8}  {"EMPATE":<8}')
                for c in pontos_jogador, pontos_pc, empates:
                    print(end=f'{c:<11}')

            elif jogador == 1:
                print('COMPUTADOR VENCE')
                pontos_pc += 1
                print(f'{"HUMANO":<8} {"MAQUINA":<8}  {"EMPATE":<8}')
                for c in pontos_jogador, pontos_pc, empates:
                    print(end=f'{c:<11}')

            elif jogador == 2:
                print('EMPATE')
                empates += 1
                print(f'{"HUMANO":<8} {"MAQUINA":<8}  {"EMPATE":<8}')
                for c in pontos_jogador, pontos_pc, empates:
                    print(end=f'{c:<11}')

        simnao('\nGostaria de continuar? [S/N] ')
