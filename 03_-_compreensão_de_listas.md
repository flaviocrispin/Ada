# Compreensão de listas e expressões geradoras

Muito do que estudamos até o momento em Python pode ser reproduzido de maneira parecida em outras linguagens. Comandos como `if`, `else`, `while` e `for`, bem como conceitos como criar funções, passar parâmetros e retornar valores são comuns a uma infinidade de linguagens de programação.

Porém, um dos objetivos da linguagem Python é realizar o máximo possível de trabalho com a menor quantidade possível de código, resultando em um código mais limpo e com menos efeitos colaterais. 

Com isso, o Python traz maneiras diferentes e mais enxutas de resolver problemas que já lidávamos bem utilizando outras técnicas. Parte dessas técnicas foi inspirada em conceitos de **programação funcional**, que será explicada um pouco melhor em um capítulo futuro.

As **compreensões de listas** e **expressões geradoras** são algumas dessas ferramentas.

## 1. Compreensão de listas

### 1.1. Compreensão de listas contendo apenas um loop

Vamos considerar um problema simples: montar uma lista com os quadrados dos números de 1 até 10. Você provavelmente resolveria esse problema da seguinte maneira:

```py
quadrados = []

for x in range(1, 11):
    quadrados.append(x**2)

print(quadrados)
print(x)
```

Note que utilizamos 3 linhas de código para criar uma lista: uma para declarar a lista, uma para percorrer alguns valores e uma para executar o cálculo e adicionar o resultado à lista.

Além disso, criamos uma variável extra, `x`, que segue existindo em nosso programa mesmo após o loop, como você pode observar pelo segundo `print` do exemplo.

A **compreensão de listas** resolve todos esses problemas: iremos resumir em uma única linha a criação da nova lista já com todos os valores desejados, e sem variáveis *sobrando* após a execução:

```py
quadrados_compreensao = [num**2 for num in range(1, 11)]

print(quadrados_compreensao)
```

Note que a variável `x`, criada na versão extensa, ainda existe. A variável `num`, utilizada na compreensão, não:

```py
print('x:', x) # imprime 10
print('num:', num) # erro de variável não existente
```

Vale destacar que você não precisa necessariamente utilizar `range` em suas compreensões. Você pode utilizar **qualquer** tipo de iterável, como listas, tuplas, strings etc.

O exemplo abaixo monta uma lista contendo a metade do valor de cada elemento de uma outra lista:

```py
numeros = [1, 9, 4, 7, 6, 2]

metades = [n/2 for n in numeros]

print(metades)
```

### 1.2. Condicionais em compreensões

Podemos utilizar compreensões em nossas condicionais. 
Imagine que não fossem aceitos valores "quebrados" no exemplo anterior. Logo, não podemos dividir os números ímpares, apenas os pares. Fazemos isso usando um `if` na expressão:

```py
metades_pares = [n/2 for n in numeros if n % 2 == 0]
print(metades_pares)
```

Podemos também utilizar `else` na expressão. Vejamos mais um exemplo: 

Considere que são aceitos números quebrados no exemplo das metades. Porém, não queremos utilizar o tipo `float` desnecessariamente. Portanto, faremos uma divisão **inteira** quando o número for par (para que o resultado seja int) e uma divisão **real** quando o número for ímpar (para que o resultado seja float). A expressão ficaria assim:

```py
metades_tipo = [n//2 if n % 2 == 0 else n/2 for n in numeros]

print(metades_tipo)
```

Note que quando usamos o `else`, a ordem da compreensão sofre uma alteração. Quando usamos apenas o `if`, ele vem após o `for`. Com o `else`, ambos vêm antes.

Outro ponto importante é que no caso do `else` passamos a ter uma segunda expressão. Quando a condição do `if` é verdadeira, a compreensão irá executar a expressão original. Caso contrário, ela irá executar a expressão do `else`.

Generalizando a sintaxe das compreensões de lista, temos as seguintes combinações:

```py
lista = [expressao for item in colecao]

# equivale a:

for item in colecao:
    lista.append(expressao)
```
---

```py
[expressao for item in colecao if condicao]

# equivale a:

for item in colecao:
    if condicao:
        lista.append(expressao)
```

---

```py
[expressao if condicao else expressao_alternativa for item in colecao] 

# equivale a:

for item in colecao:
    if condicao:
        lista.append(expressao)
    else:
        lista.append(expressao_alternativa)
```

### 1.3. Aninhando compreensões

É possível aninhar compreensões de lista. Ao colocarmos mais de um `for` consecutivo, o primeiro for será considerado o mais externo, e o seguinte, mais interno. O exemplo abaixo mostra todas as combinações possíveis entre alguns nomes e sobrenomes:

```py
nomes = ['Ana', 'Bruno', 'Carla', 'Daniel', 'Emília']
sobrenomes = ['Silva', 'Oliveira']

combinacoes = [print (nome) + ' ' + print (sobrenome) for nome in nomes for sobrenome in sobrenomes]
print(combinacoes)
```

A linha ```combinacoes = [nome + ' ' + sobrenome for nome in nomes for sobrenome in sobrenomes]``` equivale a:

```py
combinacoes = []

for nome in nomes:
    for sobrenome in sobrenomes:
        combinacoes.append(nome + ' ' + sobrenome)
```

Inclusive podemos utilizar essa forma para trabalhar com matrizes. O exemplo abaixo lê pelo teclado a quantidade de vitórias, empates e derrotas para cada time em um grupo:

```py
times = ['Atlético Python', 'JavaScript United', 'C Seniors', 'Javeiros do Norte']
entradas = ['V', 'E', 'D']

tabela = [[int(input(f'Digite a quantidade de {tipo} do time {time}: ')) for tipo in entradas] for time in times]

print(tabela)
```

### 1.4. Compreensão de dicionários

Da mesma forma que utilizamos compreensão para listas, podemos utilizá-la para dicionários. A diferença é que precisamos, obrigatoriamente, passar um par chave-valor. O exemplo abaixo parte de uma lista de notas e uma lista de alunos e chega em um dicionário associando cada aluno a uma nota.

```py
alunos = ['Ana', 'Bruno', 'Carla', 'Daniel', 'Emília']
medias = [9.0, 8.0, 8.0, 6.5, 7.0]

cadastro = {alunos[i]:medias[i] for i in range(len(alunos))}

print(cadastro)
```

Saída na tela:

```
{'Ana': 9.0, 'Bruno': 8.0, 'Carla': 8.0, 'Daniel': 6.5, 'Emília': 7.0}
```

Talvez você não tenha achado esse código tão *pythonico*, e você tem razão. Não gostamos de percorrer listas por índices dessa maneira. Uma estratégia melhor é utilizar o `zip`, estudado em capítulos anteriores:

```py
alunos = ['Ana', 'Bruno', 'Carla', 'Daniel', 'Emília']
medias = [9.0, 8.0, 8.0, 6.5, 7.0]

cadastro = {aluno:media for aluno, media in zip(alunos, medias)}

print(cadastro)
```

> 
> **Observação:** se você tentou fazer uma compreensão de dicionário e esqueceu de utilizar um par chave-valor, talvez você tenha se surpreendido ao notar que não gerou um erro. Isso ocorre porque existe *outra* estrutura de dados em Python que não estudamos no curso que utiliza os símbolos `{` e `}`: o `set` (conjunto). Ele é uma coleção **mutável** de elementos (como a lista), mas ele não possui índice (porque a ordem não importa) e ele não aceita elementos repetidos. Caso tenha curiosidade, segue material de referência com o básico de como trabalhar com conjuntos: https://www.programiz.com/python-programming/set
> 





1


