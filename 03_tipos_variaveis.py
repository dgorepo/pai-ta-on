# Não é necessário declarar o tipo de variável, o interpretador define pelo contexto.

x = 150                 # Inteiro
y = 2.3                 # Float 
z = "Eu amo Python"     # String
u = "150"               # String 

print(x, y, z)          # Apresenta o valor das variáveis na tela.

# Operações básicas

x = 10*20 + 30          

y = 2/3 - 2**3          # O operador ** significa potência.

print(10//3)

# Usando variáveis para definir novas variáveis

x = 10
y = 20
z = x + y + x*y

print(z)

# Você pode recuperar o tipo de variável

x = 10
y = "Relógio"
z = 1.2
print(type(x), type(y), type(z))
