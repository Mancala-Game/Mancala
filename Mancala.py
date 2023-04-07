from Board import *
import sys

#retorna a melhor jogada possível com minimax
def minimax(mancala, dificuldade):
    _ , move = MAX(mancala,dificuldade)
    return move

def MAX(mancala,dificuldade):
    move=None
    if mancala.fim_jogo() or dificuldade==0:
        move=mancala.last
        return mancala.utility(2),move
    
    max_value = float("-inf")
    for s in mancala.possible_moves():
        value, _ = MIN(s, dificuldade - 1)
        if  value>max_value:
            max_value=value
            move=s.last
    
    return max_value,move

def MIN(mancala,dificuldade):
    move=None
    if mancala.fim_jogo() or dificuldade==0:
        move=mancala.last
        return mancala.utility(1),move

    min_value = float("inf")
    for s in mancala.possible_moves():
        value, _ = MAX(s, dificuldade - 1)
        if value<min_value:
            min_value=value
            move = s.last
            
    return min_value,move

#retorna a melhor jogada possível com montecarlo
def montecarlo(mancala, dificuldade):
    return

#jogada Humano vs Humano
def hum_hum(mancala):
    jog = 1
    while mancala.fim_jogo() == -1:
        print(mancala)
        if (mancala.jogada_impossivel(jog)):
            jog = mancala.troca_jog(jog)
        print('Jogador %d:'%jog)
        #for i in mancala.possible_moves(jog):
        #    print(i)
        prox_jog = jog
        while prox_jog == jog and mancala.jogada_impossivel(jog)==False:
            print('Escolha a posição em que quer jogar:')
            pos = int(input())
            while pos>11 or pos<0:
                print('Posição Inválida. Insira outra posição.')
                pos = int(input())
            while pos>5 and jog == 1:
                print('Não é possível jogar na posição do adversário. Insira outra posição.')
                pos = int(input())
            while pos<6 and jog == 2:
                print('Não é possível jogar na posição do adversário. Insira outra posição.')
                pos = int(input())
            while mancala.list[pos] == 0:
                print('Não é possível jogar numa posição com 0 peças. Insira outra posição.')
                pos = int(input())
            prox_jog = mancala.move(jog, pos)
            if prox_jog == jog and mancala.jogada_impossivel(jog)==False:
                print(mancala)
                print('É o jogador %d a jogar outra vez' %jog)
        jog = prox_jog
    print('O jogo acabou.')
    if (mancala.fim_jogo() == 0):
        print('Empate.')
    else:
        print('O vencedor foi o jogador %d' %mancala.fim_jogo())
    print('Número total de jogadas: %d' %mancala.num_mov)
    sys.exit()

#Jogada Humano vs Computador
def hum_comp(mancala, estrategia, dificuldade):
    jog = 1
    while mancala.fim_jogo() == -1:
        print(mancala)
        if (mancala.jogada_impossivel(jog)):
            jog = mancala.troca_jog(jog)
        print('Jogador %d:'%jog)
        prox_jog = jog
        while prox_jog == 1 and mancala.jogada_impossivel(jog)==False:
            print('Escolha a posição em que quer jogar:')
            pos = int(input())
            while pos>11 or pos<0:
                print('Posição Inválida. Insira outra posição.')
                pos = int(input())
            while pos>5 and jog == 1:
                print('Não é possível jogar na posição do adversário. Insira outra posição.')
                pos = int(input())
            while pos<6 and jog == 2:
                print('Não é possível jogar na posição do adversário. Insira outra posição.')
                pos = int(input())
            while mancala.list[pos] == 0:
                print('Não é possível jogar numa posição com 0 peças. Insira outra posição.')
                pos = int(input())
            prox_jog = mancala.move(jog, pos)
            if prox_jog == jog and mancala.jogada_impossivel(jog)==False:
                print(mancala)
                print('É o jogador %d a jogar outra vez' %jog)
        jog = prox_jog
        while prox_jog == 2 and mancala.jogada_impossivel(jog)==False:
            if estrategia == 1:
                melhor_jogada = minimax(mancala, dificuldade)
            if estrategia == 2:
                melhor_jogada = montecarlo(mancala, dificuldade)
            prox_jog = mancala.move(jog, melhor_jogada)
            if prox_jog == jog and mancala.jogada_impossivel(jog)==False:
                print(mancala)
                print('É o jogador %d a jogar outra vez' %jog)
        jog = prox_jog
    print('O jogo acabou.')
    if (mancala.fim_jogo() == 0):
        print('Empate.')
    else:
        print('O vencedor foi o jogador %d' %mancala.fim_jogo())
    print('Número total de movimentos: %d' %mancala.num_mov)
    sys.exit()

#Jogada Computador vs Computador
def comp_comp(mancala, estrategia1, estrategia2, dificuldade):
    jog = 1
    while mancala.fim_jogo() == -1:
        print(mancala)
        if (mancala.jogada_impossivel(jog)):
            jog = mancala.troca_jog(jog)
        print('Jogador %d:'%jog)
        while prox_jog == 1 and mancala.jogada_impossivel(jog)==False:
            if estrategia1 == 1:
                melhor_jogada = minimax(mancala, dificuldade)
            if estrategia1 == 2:
                melhor_jogada = montecarlo(mancala, dificuldade)
            prox_jog = mancala.move(jog, melhor_jogada)
            if prox_jog == jog and mancala.jogada_impossivel(jog)==False:
                print(mancala)
                print('É o jogador %d a jogar outra vez' %jog)
        while prox_jog == 2 and mancala.jogada_impossivel(jog)==False:
            if estrategia2 == 1:
                melhor_jogada = minimax(mancala, dificuldade)
            if estrategia2 == 2:
                melhor_jogada = montecarlo(mancala, dificuldade)
            prox_jog = mancala.move(jog, melhor_jogada)
            if prox_jog == jog and mancala.jogada_impossivel(jog)==False:
                print(mancala)
                print('É o jogador %d a jogar outra vez' %jog)
        jog = prox_jog
    print('O jogo acabou.')
    if (mancala.fim_jogo() == 0):
        print('Empate.')
    else:
        print('O vencedor foi o jogador %d' %mancala.fim_jogo())
    print('Número total de movimentos: %d' %mancala.num_mov)
    sys.exit()


def main():
    print('Jogo Mancala')
    mancala = Board()
    print('Escolha o modo de jogo (insira o número correspondente):')
    print('1: Humano vs Humano; 2: Humano vs Computador; 3: Computador vs Computador')
    modo_jog = int(input())
    if modo_jog == 1:
        hum_hum(mancala)
    if modo_jog == 2:
        print('Escolha a estratégia para o computador (insira o número correspondente):')
        print('1: Minimax com cortes Alfa-Beta; 2: Monte Carlo')
        estrategia = int(input())
        print('Escolha a dificuldade (insira o número correspondente):')
        print('1: Fácil; 2: Médio; 3: Difícil')
        dificuldade = int(input())
        hum_comp(mancala, estrategia, dificuldade)
    if modo_jog == 3:
        print('Escolha a estratégia para o computador 1 (insira o número correspondente):')
        print('1: Minimax com cortes Alfa-Beta; 2: Monte Carlo')
        estrategia1 = int(input())
        print('Escolha a estratégia para o computador 2 (insira o número correspondente):')
        print('1: Minimax com cortes Alfa-Beta; 2: Monte Carlo')
        estrategia2 = int(input())
        print('Escolha a dificuldade (insira o número correspondente):')
        print('1: Fácil; 2: Médio; 3: Difícil')
        dificuldade = int(input())
        comp_comp(mancala, estrategia1, estrategia2, dificuldade)

if __name__ == '__main__':
    main()
