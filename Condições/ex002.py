print('Exercício 001')
print(">>> Condições <<<")

meta = 50000
qtd_vendida = int(input('Quantidade Vendida'))

if  qtd_vendida >= meta:
        print('Batemos a meta de vendas de Iphone, vendemos {} unidades!'.format(qtd_vendida))
else:
        print('Infelizmente não batemos a meta, vendemos {} unidades esses mês. A meta era de {}.'.format(qtd_vendida, meta))
