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
