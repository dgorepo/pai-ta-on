# Py tá ON !

Bem vindo ao curso Py tá ON ! Aprenda Python se divertindo.

O nome do curso diz respeito a frase dita pela minha filha de 3 anos:

*"- Filha, porque você sempre pede silêncio?"* 

*"- Papai, você sempre ta em reunião. Vive falando **pai tá ON (Python)**"*

## Sumário

- [Python](#python)
- [O que é um programa?](#o-que-e-um-programa)
- [Atribuição](#atribuicao)
- [Tipos de variáveis](#tipos-de-variaveis)
- [Nomes de variáveis](#nomes-de-variaveis)
- [Condicionais](#condicionais)
- [Comandos de repetição](#comandos-de-repeticao)
- [Funções](#funcoes)
- [Funções lambda](#topico-3)
- [Strings](#topico-3)
- [Listas](#topico-3)
- [Tuplas](#topico-3)
- [Dicionários](#topico-3)
- [Trabalhando com datas](#topico-3)

## Extras

- [Orientação a objetos](#topico-3)
- [Banco de Dados](#topico-3)
- [Numpy](#topico-3)
- [Pandas](#topico-3)
- [Tratamento de erros](#topico-3)
- [Testes de software](#topico-3)
- [Padrões de projeto](#topico-3)


## <a name="python"></a>Python

Python é uma linguagem de programação de alto nível, interpretada, orientada a objetos lançada por Guido van Rossum em 1991.

A linguagem prioriza legibilidade do código em detrimento de performance.

Atualmente é uma das linguagens de programação mais populares. Tem sido muito usada em computação científica, análise de dados, estatística e integência artificial e muito mais.

O nome Python se deve ao grupo humorístico britânico Monty Python.

### Documentação

https://www.python.org/

### Guia de estilo

https://www.python.org/dev/peps/pep-0008/

## <a name="o-que-e-um-programa"></a>O que é um programa?

Python é uma linguagem imperativa. Isso significa que você deve fazer uma lista de tarefas que ele deve executar. Por exemplo:

1. Escreva 'Computador' na tela.
2. Defina x como 40.
3. Defina y como x*234
4. Escreva y na tela.

```
print("computador") # Escreve 'Computador'
x = 40              # x recebe 40. Agora existe uma variável chamada x que vale 40.
y = x*234           # y recebe x*234
print(y)            # Escreve y
```

### Observações

* As linhas são executadas em sequência.
* O texto com as instruções é chamado de código do programa.
* Um trecho de programa também pode ser chamado de rotina.
* A numeração não faz parte do código, é colocado para conveniência do programador.
* Você pode acrescentar comentários ao código usando cerquilha (#).
* Todo texto depois da cerquilha é desconsiderados.

## <a name="atribuicao"></a>Atribuição

O comando de atribuição define ou re-define o valor armazenado no local de armazenamento indicado por um nome de variável.

- Quando escrevemos '''x = 40''', lemos x recebe 40.
- Dizemos que o símbolo = é o operador de atribuição (assignment operator)

```
# Python diferencia capitalização, isto é, letras maiúsculas e minúsculas.

soma = 3
SOMA = 40

print(soma)
print(SOMA)
```


## <a name="tipos-de-variaveis"></a>Tipos de variáveis

O Python distingue diversos tipos de variáveis: inteiros, floats, strings, listas e muito mais.

* Inteiros: números inteiros como 34, 3920 e -83829.
* Floats (ponto flutuante): Reais não necessariamente inteiros como 2.3 e -3.444. Use ponto como separador decimal.
* Strings. Sequência de caracteres como "Python" ou "computador". Use aspas duplas ou simples. Existem outras formas que veremos adiante.

```
# Não é necessário declarar o tipo de variável, o interpretador define pelo contexto.

x = 150                 # Inteiro
y = 2.3                 # Float 
z = "Eu amo Python"     # String
u = "150"               # String 

print(x, y, z)          # Apresenta o valor das variáveis na tela.
```

```
# Operações básicas

x = 10*20 + 30          

y = 2/3 - 2**3          # O operador ** significa potência.

print(10//3)
```

```
# Usando variáveis para definir novas variáveis

x = 10
y = 20
z = x + y + x*y

print(z)
```

```
# Você pode recuperar o tipo de variável

x = 10
y = "Relógio"
z = 1.2
print(type(x), type(y), type(z))
```


## <a name="nomes-de-variaveis"></a>Nomes de variáveis

* Nomes de variáveis devem ser compostos de caracteres alfanuméricos e _ (underscore).
* Não pode começar com dígitos.
* Evite caracteres acentuados e outros símbolos.
* Podem ser longos.

```
trinta = 30
_numero = 500
variavel_2 = 100
variável = 200 # possível usar outros caracteres unicode, mas não é recomendável.
```

## <a name="condicionais"></a>Condicionais

* Um bloco de código pode ser executando apenas quando uma dada condição é satisfeita;
* No python existem os comandos if, else e elif;
* A sintaxe é semelhante à do for: uso de dois pontos e indentação.

```
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
```


## <a name="comandos-de-repeticao"></a>Comandos de repetição

O Python possui duas estruturas de repetição:

* for: para executar o código em um conjunto pré-determinado de valores.
* while: para executar enquanto uma dada condição for verdadeira.

```
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

```


## <a name="funcoes"></a>Funções

Funções permitem dividir o código em partes funcionais, tornando mais claro e conciso

```
def minha_primeira_funcao(x):           # Você deve colocar um ':' ao final.
    print("Recebi o argumento x =", x)
    # print(x**2)
    return x**2     
                                        
print(minha_primeira_funcao(10))
```

```
# Uma função não precisa retornar valores

def minha_segunda_funcao(x):           # Você deve colocar um ':' ao final.
    print("Recebi o argumento x =", x) 

minha_segunda_funcao(10) # não retorna nada
```

```
# Uma função pode não receber argumentos

def sem_parametros():
    print('passei por aqui.')
    return 3

print(sem_parametros())
```

```
# Uma função pode receber muitos parametros

def muitos_parametros(x, y, z):
    return x*y + z
    

print(muitos_parametros(1, 2, 3))
```

```
# Pode-se colocar valores padrão para parâmetros
def funcao(x=10, y=20, z=3):
    return x*y + z

print(funcao())          # Implícito: funcao(10, 20, 3)
print(funcao(x=2, y=5))  # Implícito: funcao(2, 5, 3)
print(funcao(z=5))       # Implícito: funcao(10, 20, 5)
```

```
# Você pode misturar, mas os valores padrão não podem vir antes dos outros. 
def funcao(x, y=20, z=3):
    return x*y + z

print(funcao(10))       # Implícito funcao(10, 20, 3)
print(funcao(2, 5))     # Implícito funcao(2, 5, 3)
print(funcao(10, z=5))  # Implícito funcao(10, 20, 5)
# print(funcao())       # Erro
```

```
# Uma função tem acesso às variáveis definidas no contexto de onde foi chamada

def minha_funcao():
    y=5
    return x

x = 7
print(minha_funcao())
# print(y) # Erro!
```

```
# Mas variáveis criadas localmente são apenas locais e não se propagam.
# Atenção, se você atribui valor a uma variável dentro de uma função, 
# ela se torna local. 

def minha_funcao():
    global x
    x = 2
   
    # y = 3
    return x


x = 5

print("x =", x)
print("A função retornou", minha_funcao())
print("x =", x)
# print(y) # erro, experimente usar global
```

```
# Funções podem conter código estruturado e complexo como um programa qualquer
# 5! = 5.4.3.2.1 = 120,   3! = 3.2.1 = 6

def fatorial(n):
    fat = 1
    for i in range(1, n+1): # 1, 2, 3, ..., n
        fat *= i

    return fat

print("5! =", fatorial(50))
``` 

```
# Funções podem ter mais de um return

def testa(x):
    if x<10:
        return "é menor que 10."    # Acaba execução da função
   
    if x==10:
        return "é igual a 10."

    return "é maior que 10."
    
for i in range(1, 20, 3):
    print(i, testa(i))
```


```
# Funções podem chamar outras funções.
import numpy as np

def f(x):
    return x**2 + 1

def g(x):
    return f(x) + 1 + np.sin(x)

print(g(2))
```

```
# Funções podem chamar a si mesmas. 
# Cuidado com recursões!

# 5! = 5.4.3.2.1 = 5.4!, 4! = 4.3!, 3! = 3.2!, 

def fatorial (n):
    print("Recebi ", n)
    
    assert n>=0, 'n deve ser um inteiro não negativo.'
    
    if n==0 or n==1:
        return 1
    
    return n*fatorial(n-1) #n! = n(n-1)(n-2)... 5! = 5.4.3.2.1 = 5.4!, n!  = n.(n-1)!
```
