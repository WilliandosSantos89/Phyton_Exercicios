print('Exercício 004')

meta = 20000
valor_vendido = int(input('Valor vendido: R$  '))
bonus_3 = valor_vendido + (valor_vendido * 0.03)
bonus_7 = valor_vendido + (valor_vendido * 0.07)

if valor_vendido < meta:
    print('Infelizemente você não atingiu a meta e não terá bônus.')

elif valor_vendido > 2 * meta:
    print('Parabéns, você atingiu o dobro do valor da meta. Seu bônus será de 7% sobre o '
          'valor da venda. O valor ficará em R$ {:.2f}.'.format(bonus_7))
else:
    valor_vendido > meta
    print('Parabéns, você atingiu a meta e ganhará 3% '
          'de aumento sobre o valor que '
          'vendeu. Seu bônus será de R$ {:.2f}.'.format(bonus_3))



