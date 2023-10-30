#Verificação Letra maiuscula e minuscula
from tabnanny import check


def check_char(text):
    type = {"Uppercase":0, "Lowercase":0}
    for char in text:
        if char.isupper():
            type["Uppercase"] += 1
        elif char.islower():
            type["Lowercase"] += 1
        print("Texto Original", text)
        print("Número de letras maiusculas: ", type["Uppercase"])
        print("Número de letras minúsculas: ", type["Lowercase"])
        
#check_char("A melhor forma de prever o futuro é Criá-lo")

#Verifica numero par ou impar

def check_number(numbers):
    pairs = []
    odd = []
    for number in numbers:
        if number % 2 == 0:
            pairs.append(number)
        else:
            odd.append(number)
    return pairs, odd
print(check_number([1,2,5,7,9,13,15,18]))