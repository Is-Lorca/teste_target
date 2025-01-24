'''
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou 
pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
'''

def invertendo(palavra):
    palavra_invertida = ''
    for letra in palavra:
        palavra_invertida = letra + palavra_invertida
    return palavra_invertida

palavra = input('Insira a palavra que deseja inverter: ')
#Palavra Teste: Parafernalha

resposta = invertendo(palavra)
print(resposta)

#Resposta com base no teste: ahlanrefaraP