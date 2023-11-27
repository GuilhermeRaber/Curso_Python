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


cpf = input("CPF a conferir:")
cpf1 = str(cpf[:9])
cpflista=list(cpf1)
if len(cpf1) == 9:
    contador = 10
    soma=0
    calculo=0
    for digito in cpf1:
        calculo += contador * int(digito) * 10
        contador -= 1
    resto = calculo % 11
    digito1 = resto if resto <= 9 else 0
    
    print(f'O primeiro dígito é {digito1}')

else:
    print('Erro! Numero invalido.')
calculo2=0
cpfnovo = list(cpf1)
cpfnovo.append(digito1)
contador2 = 11
for digito in cpfnovo:
    calculo2 += contador2 * int(digito) * 10
    contador2 -= 1
resto2 = calculo2 % 11
digito2 = resto2 if resto2 <= 9 else 0
cpfnovo.append(digito2)
print(f'O segundo dígito é {digito2}')

cpffinal = (f'{cpf1}{digito1}{digito2}')
print(cpffinal)

if cpf == cpffinal:
    print('O CPF é válido')
else:
    print('O CPF não é válido')