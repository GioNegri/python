name = input("Digite o nome do Jogo\n")
yearLaunch = int(input("Digite o ano de lançamento do jogo\n")) 
gamePrice = float(input("Digite o preço do jogo \n"))
planIncluded = input("Está incluso no plano?\n")

print("###Dados do Jogo####")
print("####################")
#Alternativa 1

# print("Nome do jogo: ",name)
# print("Ano de lançamento: ",yearLaunch)
# print("Preço do jogo: ",gamePrice)
# print("Está incluso no plano? ",planIncluded)

#Alternativa 2

#print (
# "Nome do Jogo: ", name,
# "\nAno de lançamento:", yearLaunch,
# "\nPreço do jogo",gamePrice,
# "\nEstá incluso no plano?", planIncluded
# )

#Alternativa 3

print(f" Nome do Jogo: {name} \n Ano Lançamento: {yearLaunch} \n Preço do jogo: {gamePrice} \n Está incluso no plano? {planIncluded}")