#1 - Função  para imprimir hello world
def welcome():
    print("Hello world")
    
welcome()

# 2 - Função para somar dois numeros

def sum():
    #print (5+4)
    return 5 + 4

print(sum())

# 3 - Função para cadastrar um jogo

def create_game():
    name = input("Digite o nome do Jogo\n")
    yearLaunch = int(input("Digite o ano de lançamento do jogo\n")) 
    gamePrice = float(input("Digite o preço do jogo \n"))
    noteRating = input("Digite a nota de avaliação do jogo: \n")
    print(f"{name} - R$ {gamePrice} ")
    
create_game()