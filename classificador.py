nome = input('Qual o seu nome?')
xp = int(input('Quanto de xp voce tem?'))

if (xp <= 1000): {
    print(f'O Herói de nome {nome} está no nível de Ferro')
}

if (xp >1000 and xp <= 2000): {
    print(f'O Herói de nome {nome} está no nível de Bronze')
}

if (xp >2000 and xp <= 5000): {
    print(f'O Herói de nome {nome} está no nível de Prata')
}

if (xp >5000 and xp <= 7000): {
    print(f'O Herói de nome {nome} está no nível de Ouro')
}

if (xp >7000 and xp <= 8000): {
    print(f'O Herói de nome {nome} está no nível de Platina')
}
    
if (xp >8000 and xp <= 9000): {
    print(f'O Herói de nome {nome} está no nível de Ascendente')
}

if (xp >9000 and xp <= 10000): {
    print(f'O Herói de nome {nome} está no nível de Imortal')
}
    
if (xp >= 10001): {
    print(f'O Herói de nome **{nome} está no nível de Radiante')
}