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
- [Condicionais](#topico-3)
- [Comandos de repetição](#topico-3)
- [Funções](#topico-3)
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
