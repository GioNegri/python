"""
*args - Utilizamos ele qnd nao temos certeza de quantos argumentos queremos ter numa função.
-- Os argumentos sao passados como uma tupla

**kwargs - Além dos valores podemos passar tambem as respectivas chaves para cada argumento.
-Os argumentos sao passados como um dicionario
"""

# 1 - Soma de números



from unicodedata import category, name


def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"Soma é: {sum_total} ")
sum(7,10,11)

# 2 - Apresentação de cursos
def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value} ")

print("###Cursos###")
        
presentation(name= "Python" , category = "Backend", Level = "Iniciante")
presentation(name= "Visão computacional com Python" , category = "IA", Level = "Avançado")