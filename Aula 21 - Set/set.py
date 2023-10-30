gamesSet = { "fifa 23" , "Red dead 2" , "Star Wars" , "Mario"}

print(gamesSet)

# 1 - Buscar o tamanho do set

print(len(gamesSet))

# 2 - True e 1 são considerados o mesmo valor
exampleSet = { "fifa 23" , True ,1, 90.50}
print(exampleSet)

# 3 - Adicionar item de outro set
gamesSet.update(exampleSet)
print(gamesSet)

# 4 - Remover um item no set

gamesSet.remove(True)
gamesSet.remove(90.50)
print(gamesSet)

# Não possibilita recuperar valores via fatiamento ou slice