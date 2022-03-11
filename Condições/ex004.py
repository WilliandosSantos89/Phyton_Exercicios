print('Exercício 004')

meta = 5000
valor_vendido = int(input('Valor vendido: '))
bonus_3 = valor_vendido * 0.3
bonus_7 = valor_vendido * 0.7

if valor_vendido >= meta:
    print('Parabéns, você atingiu a meta e ganhará 3% '
          'de aumento sobre o valor que '
          'vendeu. Seu bônus será de {}.'.format(bonus_3))
elif valor_vendido

