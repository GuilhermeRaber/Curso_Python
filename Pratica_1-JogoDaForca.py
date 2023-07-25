"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.

Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.

Quando o usuário digitar uma letra, você vai conferir se a letra digitada está
na palavra secreta.

Se a letra digitada estiver na palavra secreta, exiba a letra;

Se a letra digitada não estiver na palavra secreta, exiba *.

Faça a contagem de tentativas do seu usuário.

Extras: Opção de jogar novamente; Seleção de dificuldades.
"""


escolha = int(input('Escolha uma dificuldade: 0. Noob, 1. Facil, 2. Medio, 3. Dificil ou 4. Boss: '))
dificuldade = ['Noob', 'Fácil', 'Médio', 'Difícil', 'Boss']
dificuldades = ['cano', 'mouse', 'machado', 'estofador', 'procrastinar']
comprimentos = [4, 5, 6, 8, 9]

while escolha not in range(len(dificuldades)):
    print('Digite uma opção válida!')
    escolha = int(input('Escolha uma dificuldade: 0. Noob, 1. Facil, 2. Medio, 3. Dificil ou 4. Boss: '))
      
palavra = dificuldades[escolha]
comprimento = comprimentos[escolha]

print(f'Jogo iniciado! A dificuldade é: {dificuldade[escolha]}.')
print(f'A palavra secreta tem {len(palavra)} letras. Boa Sorte!')

acertos = ''
i=0

while True:
    if i <= 15:

        i += 1

        letra = input(f'Tentativa número {i}. Digite uma letra: ')

        if len(letra) > 1:
            print('Voce digitou mais de uma letra')
            continue

        elif letra in palavra:
            print(f'A letra {letra} está na palavra')

            acertos += letra
            palavra_formada = ''

            for letra in palavra:
                if letra in acertos:
                    palavra_formada += letra
                else:
                    palavra_formada += '*'

            print(palavra_formada.upper())

            if len(acertos) == comprimento:
                palavra = palavra.upper()
                print(f'PARABÉNS! VOCÊ GANHOU!')
                print(f'Você acertou a palavra {palavra} inteira em {i} tentativas!')

                repetir = input('Você gostaria de jogar novamente? S-Sim, N-Não: ')
                repetir = repetir.upper()

                while repetir != 'S' and repetir != 'N':
                    print('Opção inválida.')
                    repetir = input('Você gostaria de jogar novamente? S-Sim, N-Não: ')
                    repetir = repetir.upper()

                if repetir == 'S':
                    escolha = int(input('Escolha uma dificuldade: 0. Noob, 1. Facil, 2. Medio, 3. Dificil ou 4. Boss: '))
                    dificuldade = ['Noob', 'Fácil', 'Médio', 'Difícil', 'Boss']
                    dificuldades = ['cano', 'mouse', 'machado', 'estofador', 'procrastinar']
                    comprimentos = [4, 5, 6, 8, 9]

                    while escolha not in range(len(dificuldades)):
                        print('Digite uma opção válida!')
                        escolha = int(input('Escolha uma dificuldade: 0. Noob, 1. Facil, 2. Medio, 3. Dificil ou 4. Boss: '))
                        
                    palavra = dificuldades[escolha]
                    comprimento = comprimentos[escolha]

                    acertos = ''
                    i = 0

                    print(f'Jogo iniciado! A dificuldade é: {dificuldade[escolha]}.')
                    print(f'A palavra secreta tem {len(palavra)} letras. Boa Sorte!')

                    continue

                else:                
                    print('Obrigado por jogar!')
                    break

        else:
            print(f'A letra {letra} não está na palavra')

    else:
        print(f'Voce atingiu o limite de 15 tentativas. A palavra secreta era: {palavra}')

        repetir = input('Você gostaria de jogar novamente? S-Sim, N-Não: ')
        repetir = repetir.upper()

        while repetir != 'S' and repetir != 'N':
            print('Opção inválida.')
            repetir = input('Você gostaria de jogar novamente? S-Sim, N-Não: ')
            repetir = repetir.upper()

        if repetir == 'S':
            escolha = int(input('Escolha uma dificuldade: 0. Noob, 1. Facil, 2. Medio, 3. Dificil ou 4. Boss: '))
            dificuldade = ['Noob', 'Fácil', 'Médio', 'Difícil', 'Boss']
            dificuldades = ['cano', 'mouse', 'machado', 'estofador', 'procrastinar']
            comprimentos = [4, 5, 6, 8, 9]

            while escolha not in range(len(dificuldades)):
                print('Digite uma opção válida!')
                escolha = int(input('Escolha uma dificuldade: 0. Noob, 1. Facil, 2. Medio, 3. Dificil ou 4. Boss: '))
                    
            palavra = dificuldades[escolha]
            comprimento = comprimentos[escolha]
            acertos = ''
            i = 0

            print(f'Jogo iniciado! A dificuldade é: {dificuldade[escolha]}.')
            print(f'A palavra secreta tem {len(palavra)} letras. Boa Sorte!')
            continue

        else:     
            print('Obrigado por jogar!')           
            break