from random import choice
from time import sleep

jogar = ['papel', 'pedra', 'tesoura']
pontos_do_computador = 0
pontos_do_jogador = 0
jogadas = 0
rodada = 1
def computadorJoga():
    computador = choice(jogar)
    return computador

def Linhas():
    print('-'*100)

def jogaPedra():
    global pontos_do_computador
    global pontos_do_jogador
    if computadorjoga == 'tesoura':
        print(f'COMPUTADOR: {computadorjoga}')
        print(f'{nome_jogador}: pedra')
        print(f'PEDRA mata TESOURA - PONTO PARA {nome_jogador}!')
        pontos_do_jogador = pontos_do_jogador + 1

    elif computadorjoga == 'pedra':
        print(f'COMPUTADOR: {computadorjoga}')
        print(f'{nome_jogador}: pedra')
        print('PEDRA igual PEDRA - Empate: Ninguem pontua!')
    
    else:
        print(f'COMPUTADOR: {computadorjoga}')
        print(f'{nome_jogador}: pedra')
        print('PAPEL mata PEDRA - PONTO PARA COMPUTADOR!')
        pontos_do_computador = pontos_do_computador + 1

def jogaPapel():
    global pontos_do_computador
    global pontos_do_jogador
    if computadorjoga == 'pedra':
        print(f'COMPUTADOR: {computadorjoga}')
        print(f'{nome_jogador}: papel')
        print(f'PAPEL mata PEDRA - PONTO PARA {nome_jogador}!')
        pontos_do_jogador = pontos_do_jogador + 1

    elif computadorjoga == 'papel':
        print(f'COMPUTADOR: {computadorjoga}')
        print(f'{nome_jogador}: papel')
        print('PAPEL igual PAPEL - Empate: Ninguem pontua!')
    
    else:
        print(f'COMPUTADOR: {computadorjoga}')
        print(f'{nome_jogador}: papel')
        print('TESOURA mata PAPEL - PONTO PARA COMPUTADOR!')
        pontos_do_computador = pontos_do_computador + 1

def jogaTesoura():
    global pontos_do_computador
    global pontos_do_jogador
    if computadorjoga == 'papel':
        print(f'COMPUTADOR: {computadorjoga}')
        print(f'{nome_jogador}: tesoura')
        print(f'TESOURA mata PAPEL - PONTO PARA {nome_jogador}!')
        pontos_do_jogador = pontos_do_jogador + 1

    elif computadorjoga == 'tesoura':
        print(f'COMPUTADOR: {computadorjoga}')
        print(f'{nome_jogador}: tesoura')
        print('TESOURA igual TESOURA - Empate: Ninguem pontua!')
    
    else:
        print(f'COMPUTADOR: {computadorjoga}')
        print(f'{nome_jogador}: tesoura')
        print('PEDRA mata TESOURA - PONTO PARA COMPUTADOR!')
        pontos_do_computador = pontos_do_computador + 1

def verificarVencedor():
    if pontos_do_computador > pontos_do_jogador:
        print(f'E o VENCEDOR foi o Computador com {pontos_do_computador} ponto(s)!')
    else:
        print(f'PARABÉNS - O VENCEDOR foi {nome_jogador} com {pontos_do_jogador} ponto(s)!')

def jogarNovamente():
    global pontos_do_computador
    global pontos_do_jogador
    global jogadas
    global rodada
    pontos_do_computador = 0
    pontos_do_jogador = 0
    jogadas = 0
    rodada = 1
    


while True:
    print('----------JO-KEN-PÔ----------')
    

    while True:
        if jogadas == 0:
            nome_jogador = input('Digite seu nome: ')
        Linhas()
        print(f'{rodada}º Rodada')
        Linhas()
        print('[1] - Pedra')
        print('[2] - Papel')
        print('[3] - Tesoura')
        jogador = int(input('Qual a sua opção? - Digite "0" para encerrar o jogo: '))

        computadorjoga = computadorJoga()
        Linhas()
        print('JO', end='')
        sleep(1)
        print('KEN', end='')
        sleep(1)
        print('PÔ')

        if jogador == 1:
            jogaPedra()
            jogadas+=1
            rodada+=1

        elif jogador == 2:
            jogaPapel()
            jogadas+=1
            rodada+=1

        elif jogador == 3:
            jogaTesoura()
            jogadas+=1
            rodada+=1

        if jogador == 0:
            Linhas()
            print('OBRIGADO POR JOGAR')
            print(f'Vocês jogaram {jogadas} rodada(s)!')
            vencedor = verificarVencedor()
            Linhas()
            break
        sleep(3)            
    jogar_novamente = input('Deseja jogar novamente? (s/n) ').lower()
    if jogar_novamente == 'n':
        break
    else:
        Linhas()
        jogarNovamente()