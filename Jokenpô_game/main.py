import random
from ui.menu import valida_int, borda
from services.logica import vencedor

borda('🎮 JOKENPÔ')
borda('1 = Pedra | 2 = Papel | 3 = Tesoura')

v1, v2, empate = 0, 0, 0  #Placar global limpo

jogadas_feitas = 0
while jogadas_feitas < 5:    
    jogadas_feitas += 1
#While true: para jogos indefinidos   
    jogador1 = valida_int('Escolha sua jogada:', 0, 3)
    if jogador1 not in [1, 2, 3]:
        break

    jogador2 = random.randint(1, 3)
    print(f"Sua jogada: {jogador1} | Máquina: {jogador2}")

    #Pega resultado da rodada
    resultado = vencedor(jogador1, jogador2)
    
    #ÚNICO local que atualiza placar
    v1 += resultado[0]
    v2 += resultado[1]
    empate += resultado[2]
    
    print(f" Placar atual: Você({v1}) x Máquina({v2}) | Empates: {empate}\n")

    #Placar final
print(f'\n🏆 PLACAR FINAL:')
print(f'Vitórias Jogador 1: {v1}')
print(f'Vitórias Jogador 2: {v2}')
print(f'Empates: {empate}')
print(f'Total de jogadas: {v1 + v2 + empate}')