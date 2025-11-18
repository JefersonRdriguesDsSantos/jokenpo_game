def valida_int(pergunta: str, min: int, max: int) -> int:
    '''
    Validação de entrada dos valores, caso não atendida entra em loop.
    '''
    while True:
        try:
            valor = int(input(pergunta))
            if min <= valor <= max:
                return valor
            print(f"Erro: Digite entre {min} e {max}.")
        except ValueError:
            print('Erro: Digite um número válido')

def borda(texto: str) -> None:
    '''
    Borda criada para o menu.
    '''
    tam = len(texto)
    if tam:
        print('+' + '-' * 40 + '+')
        print('|' + texto.center(40) + '|')
        print('+' + '-' * 40 + '+')