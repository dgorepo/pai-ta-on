# Exemplo com if (if = se)

x = 5

if x > 4:
    print("x é maior que 4.") 

print('aqui')

# and = e, ambas condições devem ser satisfeitas simultaneamente.

x = 10
y = 1

if x > 4 and y < 4:
    print("x é maior que 4 e y é menor que 4.")

# or = ou, pelo menos uma das condições deve ser satisfeita.

x = 10
y = 10

if x > 4 or y < 4:
    print("x é maior que 4 ou y é menor que 4.")
    
# if e else, else = senão

x = 4

if x > 4:
    print("x é maior que 4.")
else:       # if e else ficam no mesmo nível de indentação. 
    print("x não é maior que 4.") # Executa se condição é falsa
    
# if, elif e else

x = 5

if x > 4:
    print("x é maior que 4.")
elif x == 4:                        
    print("x é igual a 4.") # Se a primeira condição é falsa e a outra é verdadeira
else:
    print("x menor que 4.") # Se ambas condições são falsas

# Dica: você pode usar quantos elif's forem necessários.


x = "Carla"

if   x == "Fabio":
    print("Porto Alegre")

elif x == "Sylvia" or x == "Daniela":
    print("São Paulo")

elif x == "Marcos":
    print("Paraná")
    
else:
    print("Não sei.")
    
# Operador ternário. https://en.wikipedia.org/wiki/%3F:

# Considere o problema

x = -1
if x>0:
    y = 'x é positivo.'
else:
    y = 'x não é positivo'

print(y)

# Operador ternário valor_a if condição else valor_b

x = 3
y = 'x é positivo.' if x > 0 else 'x não é positivo.'
print(y)

x = -5

y = 0 if x>0 else -1  # Para linguagens com sintaxe C: x>0 ? 0 : -1

print(y)

# isto é equivalente a

if x>0:
    y = 0
else:
    y = -1
 

