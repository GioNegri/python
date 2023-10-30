import pprint

gamesDict = {
    "resident evil 4" : {
        "yearLaunch" : 2023,
        "classification" : 9.8,
        "genre" : ["ação"]
    },
    "mario" : {
        "yearLaunch" : 2017,
        "classification" : 10.0,
        "genre" : ["aventura"]
    },
    "fifa 23 " : {
        "yearLaunch" : 2022,
        "classification" : 10.0,
        "genre" : ["esporte"]
    }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDict)

# 1 - Buscar informação  do dicionario aninhado
print(gamesDict["mario"]["genre"])

# 2 - Adicionar novo item
gamesDict["mario"]["players"] = 1
print(gamesDict["mario"])

# 3 - Excluir um dicionario

del gamesDict [ "resident evil 4"]
pp.pprint(gamesDict)