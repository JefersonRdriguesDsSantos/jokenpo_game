def vencedor(Jogador1, Jogador2):
    """Retorna resultado da rodada SEM modificar placar global"""
    if Jogador1 == Jogador2:
        print("🤝 EMPATE!")
        return [0, 0, 1]

    elif (Jogador1 == 1 and Jogador2 == 3) or \
         (Jogador1 == 2 and Jogador2 == 1) or \
         (Jogador1 == 3 and Jogador2 == 2):
        print("🎉 Jogador 1 VENCEU!")
        return [1, 0, 0]
    
    else:
        print("🎉 Jogador 2 VENCEU!")
        return [0, 1, 0]
