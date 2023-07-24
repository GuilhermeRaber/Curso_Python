"""Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na palavra secreta, exiba a letra;
    - Se a letra digitada não estiver na palavra secreta, exiba *.
Faça a contagem de tentativas do seu usuário."""

"""
- Definir uma ou mais palavras secretas para serem usadas para o jogo;
    pode ser usado 5 palavras em diferentes dificuldades, pedindo para o usuario escolher a dificuldade do jogo;
    dificuldade de 1 a 5, com palavras de 6, 7, 8, 10 e 12 letras com o mesmo numero de tentativas;
- Pedir uma letra para o usuario;
    adicionar uma volta ao contador de tentativas;    
- Verificar se a letra está na composicao da palavra secreta;
    verificar se o contador já chegou no limite de tentativas;
- Caso estiver, exibir a letra, caso não estiver, avisar que não está;
- proxima rodada;

"""

i=0
escolha = input('Escolha uma palavra de 1 a 3: ')
if escolha == '1': 
    palavra = 'facil'
    comprimento = 5
elif escolha == '2': 
    palavra = 'facilimo'
    comprimento = 7
elif escolha == '3': 
    palavra = 'facilissimo'
    comprimento = 8
else: 
    print('escolha uma opção válida!')

try:
    print(palavra)
except:
    while escolha != "1" and escolha != "2" and escolha != "3":
        print('Digite uma opção válida!')
        escolha = input('Escolha uma palavra de 1 a 3: ')
        if escolha == "1": 
            palavra = 'facil'
            comprimento = 5
        elif escolha == "2": 
            palavra = 'facilimo'
            comprimento = 7
        elif escolha == "3": 
            palavra = 'facilissimo'
            comprimento = 8

acertos = ''
while True:
    if i < 15:
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
                    # print(letra)
                    palavra_formada += letra
                    # print(palavra_formada)
                else:
                    # print('*')
                    palavra_formada += '*'
                    # print(palavra_formada)
            print(palavra_formada)
            if len(acertos) == comprimento:
                print(f'GANHOU! Você acertou a palavra {palavra} inteira em {i} tentativas!')
                break
        else:
            print(f'A letra {letra} não está na palavra')
    else:
        print(f'Voce atingiu o limite de 15 tentativas. A palavra secreta era: {palavra}')
        break