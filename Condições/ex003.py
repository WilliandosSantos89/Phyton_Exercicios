meta = 0.05
taxa = 0
rendimento = int(input('Taxa de redimento:'))

if rendimento > meta:
    if rendimento > 0.20:
        taxa = 0.04
        print('A taxa foi de {:.2}%.'.format(taxa))
    else:
        taxa = 0.02
        print('A taxa foi de {:.2}%.'.format(taxa))
else:
    taxa = 0
    print('A taxa foi de {}%.'.format(taxa))