gameName = "Fifa23"
gameDescription = """
    Fifa 23 é um jogo de futebol,
    desenvolvido pela EA Sports,
    e que possibilita jogar localmente ou online
"""

print(gameName.upper()) #Retornar String em maiúsculo
print(gameName.lower()) #Retornar String em mainúsculo
print(gameName.capitalize()) #Retornar primeira letra da String em maiúsculo
print(gameName.title()) #Retornar primeira letra da String em maiúsculo
print(gameName.center(10, '-'))
print(gameName.find("a")) # Retorna a posição de um determinado caractere
print(gameDescription.count("f"))
print(gameDescription.count("a"))
print(gameDescription.replace("Fifa","Pes"))
print(gameDescription.split(","))