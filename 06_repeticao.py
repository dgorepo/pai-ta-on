# Comando for
# O comando for repete um bloco de código para um conjunto pré-determinado
# de valores.

lista = [1, 2, 'Casa', 2.3]

for x in lista:         # Termine com dois pontos(:)
    print(x)            # Indente os comandos que serão repetidos.
                        # Indentação = espaços à esquerda

# Laço for com faixa de valores (range).

for x in range(10):   # Aberto à direito, isto é, não inclui 10. 
    print(x) 

# Calcula fatorial:
# Exemplo: 4! = 1x2x3x4 = 24, 5! = 1x2x3x4x5 = 120

fatorial = 1
n = 6

for i in range(1, n+1):   # Não inclui n porque o intervalo é aberto à direita.
    fatorial *= i            # fatorial = fatorial * i
    print("i = ", i, ":   i! = ", fatorial)
    
fatorial = 1
for i in range(1, 6):
    fatorial *= i
    print(i, fatorial)

    print('aqui')
    
# Exemplo com strings:

palavra = 'Alegria'
for c in palavra:   # Itera nos caracteres da string
    print(c)
    
# Mais um exemplo:

palavra = 'Teclado'
# palavra = input("Entre com uma string: ")

for i in range(1, len(palavra)+1):
    print(palavra[0:i])

    
# While 
# Executa repetidas vez um bloco código enquanto uma dada condição é verdadeira

x = 0
while x<10:   # Repete enquanto x<10
    print(x)
    x += 2

print(x)

x = 0
j = 0
while x<95: 
    x = alea.integers(100)
    print(j, x, sep=':\t')
    j += 1
    

s = 'a'
while s[0] in 'aeiou':
    s = input("Entre com uma palavra de pelo menos 5 letras: ")
    
#Testa se n é primo
import numpy as np

def teste_de_primalidade(n): # um número >1 é primo se for divisível apenas por 1 e por si mesmo
    raiz = int(np.sqrt(n))

    if n == 1:
         return False
    if n == 2:
        return True
    if n%2 == 0:        # % = resto da divisão inteira
        return False

    k = 3
    while (k<=raiz):  # testa divisibilidade por 3, 5, 7, 9, 11 etc 
        if n%k == 0:
            return False
        k += 2
    return True

n = 0
itens_a_contar = 30
for i in range(1, itens_a_contar):
    if teste_de_primalidade(i):
        print(i, "é primo.")
        n += 1

print('Existem', n, 'primos até', itens_a_contar, '.')
