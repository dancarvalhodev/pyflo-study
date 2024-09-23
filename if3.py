total_jogos = int(input('Digite o total de jogos que você possuí na Steam: '))

if total_jogos >= 1 and total_jogos <= 50:
    print('Dentro do aceitável')
else:
    print('Muitos jogos para alguém que apenas joga CS...')