"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""


cpf = input("Digite os 9 primeiros dígitos do CPF a conferir:")
cpf1 = str(cpf)
cpflista=list(cpf1)
print(f'O CPF digitado foi: {cpf} _ _')
if len(cpf1) == 9:
    i=0
    contador = 10
    soma=0
    multiplicacao = []
    while contador >= 2:
        calculo = contador * int(cpflista[i])
        multiplicacao.append(calculo)
        contador = contador-1
        i = i+1
    soma = sum(multiplicacao) * 10
    resto = soma % 11
    if resto > 9:
        digito1 = 0
        print('O primeiro dígito é 0')
    else:
        digito1 = resto
        print(f'O primeiro dígito é {digito1}')
    print(f'O CPF atualizado é: {cpf} {digito1} _')

else:
    print('Erro! Numero invalido.')