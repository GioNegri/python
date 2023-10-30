gameName = "Fifa 23"
gameDescription = """
    Fifa 23 é um jogo de futebol
    desenvolvido pela EA Sports
    e que possibilita jogar localmente ou online
"""

#string [inicio:fim] - indice começa na posição 0 /indice final -1

#1 -busque toda string a partir da primeira posição

print(gameName[0: ])

#2 - Busque string até a ultima posição
print(gameName[ : 7])

#3- Busque toda string da terceira ate a ultima posição
print(gameName[2:])

"""
string[inicio:fim:passo] -indice começa na posicao 0 / indice final -1
passo - determina o incremento. Por padrão esse numero é o 1.
"""

#4 Busque toda a string de 2 em 2 caracteres

print(gameName[::2])

#5 Busque toda a string nos indices impares
print(gameName[1::2])

#6 - Inverter uma string de tras para frente
print(gameName[::-1])