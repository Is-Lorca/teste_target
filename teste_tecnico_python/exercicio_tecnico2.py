'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 
1 e o próximo valor sempre será a soma dos 2 valores 
anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
escreva um programa na linguagem que desejar onde, 
informado um número, ele calcule a sequência de Fibonacci 
e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
'''
def sequencia_fibonacci(limite):
    sequencia = [0, 1]
    while sequencia[-1] < limite:
        sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia

def pertence_a_fibonacci(numero):
    sequencia = sequencia_fibonacci(numero)
    return numero in sequencia

numero = int(input("Insira um número para verificar se pertence à sequência de Fibonacci: "))
# Inserido no teste: 20

if pertence_a_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

#Resposta com base no teste: O número 20 NÃO pertence à sequência de Fibonacci.