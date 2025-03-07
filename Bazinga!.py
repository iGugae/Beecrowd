def jogo(sheldon, raj):
    if (sheldon == raj):
        resposta = 'De novo'
    elif (sheldon == 'pedra'):
        if (raj == 'papel' or raj == 'Spock'):
            resposta = 'Raj trapaceou'
        else:
            resposta = 'Bazinga'
    elif (sheldon == 'papel'):
        if (raj == 'pedra' or raj == 'Spock'):
            resposta = 'Bazinga'
        else:
            resposta = 'Raj trapaceou'
    elif (sheldon == 'tesoura'):
        if (raj == 'pedra' or raj == 'Spock'):
            resposta = 'Raj trapaceou'
        else:
            resposta = 'Bazinga'
    elif (sheldon == 'lagarto'):
        if (raj == 'pedra' or raj == 'tesoura'):
            resposta = 'Raj trapaceou'
        else:
            resposta = 'Bazinga'
    else:
        if (raj == 'pedra' or raj == 'tesoura'):
            resposta = 'Bazinga'
        else:
            resposta = 'Raj trapaceou'
    return resposta

num = int(input())

for i in range(0,num):
    sheldon, raj = input().split()

    resposta = jogo(sheldon,raj)
    print(f'Caso #{i+1}: {resposta}!')
