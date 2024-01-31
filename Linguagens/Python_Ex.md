# Exercícios de Python

A função `print()` desempenha um papel fundamental para imprimir texto e variáveis no console ou em outro local de saída. Ao longo das diferentes versões do Python, a sintaxe e os recursos dessa função evoluíram, oferecendo diversas maneiras de formatar e exibir mensagens.

Para praticar essa função, criamos a seguir uma lista de atividades (não obrigatórias) focada em prática para melhorar ainda mais sua experiência de aprendizagem. Bora praticar então?

## Exercícios de Print

1. Imprima a frase: Python na Escola de Programação da Alura.
2. Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.
3. Imprima a palavra: ‘ARTHUR’ de modo que cada letra fique em uma linha, como mostrado a seguir:
* A
* R
* T
* H
* U
* R

4. Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável e arredondado para apenas duas casas decimais. Para facilitar, utilize:
```python
pi = 3.14159

```

# Exercícios de Condicionais em Python

As estruturas condicionais, como `if`, `elif` e `else`, são fundamentais para a lógica de programação, permitindo que o código reaja de maneiras diferentes dependendo das condições atuais. Essas estruturas são usadas para testar se uma condição é verdadeira ou falsa e executar um bloco de código correspondente.

Para ajudar a aprimorar suas habilidades com essas estruturas, criamos uma lista de exercícios práticos. Vamos praticar?

1. Solicite ao usuário que insira um número e, em seguida, use uma estrutura `if else` para determinar se o número é par ou ímpar.
2. Pergunte ao usuário sua idade e, com base nisso, use uma estrutura `if elif else` para classificar a idade em categorias de acordo com as seguintes condições:
    - Criança: 0 a 12 anos;
    - Adolescente: 13 a 18 anos;
    - Adulto: acima de 18 anos.
3. Solicite um nome de usuário e uma senha e use uma estrutura `if else` para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
4. Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura `if elif else` para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:
    - Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
    - Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
    - Terceiro Quadrante: os valores de x e y devem ser menores que zero;
    - Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
    - Caso contrário: o ponto está localizado no eixo ou origem.

# Exercícios de Python

## Exercícios de Listas e Loops

Listas são estruturas de dados que armazenam uma coleção de itens. Elas são muito úteis quando você precisa armazenar um conjunto de elementos que podem ser de diferentes tipos (inteiros, strings, etc). Os loops, por outro lado, são estruturas de controle que permitem executar um bloco de código várias vezes.

Aqui estão alguns exercícios para praticar esses conceitos:

1. Crie uma lista para cada informação a seguir:
    - Lista de números de 1 a 10;
    - Lista com quatro nomes;
    - Lista com o ano que você nasceu e o ano atual.
2. Crie uma lista e utilize um loop `for` para percorrer todos os elementos da lista.
3. Utilize um loop `for` para calcular a soma dos números ímpares de 1 a 10.
4. Utilize um loop `for` para imprimir os números de 1 a 10 em ordem decrescente.
5. Solicite ao usuário um número e, em seguida, utilize um loop `for` para imprimir a tabuada desse número, indo de 1 a 10.
6. Crie uma lista de números e utilize um loop `for` para calcular a soma de todos os elementos. Utilize um bloco `try-except` para lidar com possíveis exceções.
7. Construa um código que calcule a média dos valores em uma lista. Utilize um bloco `try-except` para lidar com a divisão por zero, caso a lista esteja vazia.

## Exercícios de Dicionários

Dicionários são estruturas de dados que armazenam pares de chave-valor. Eles são úteis quando você precisa associar valores a chaves para recuperá-los de maneira eficiente.

1. Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
2. Utilizando o dicionário criado no item 1:
    - Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
    - Adicione um campo de profissão para essa pessoa;
    - Remova um item do dicionário.
3. Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.
4. Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
5. Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

## Exercícios de Docstrings

Docstrings são uma maneira de documentar suas funções, métodos, módulos e classes. Eles são uma ferramenta essencial para qualquer desenvolvedor Python, pois permitem que outros desenvolvedores entendam o que seu código faz.

1. Crie uma docstring para a função `exibir_nome_do_programa()`
2. Crie uma docstring para a função `exibir_opcoes()`
3. Crie uma docstring para a função `finalizar_app()`
4. Crie uma docstring para a função `opcao_invalida()`
5. Crie uma docstring para a função `exibir_subtitulo(texto)`
6. Crie uma docstring para a função `cadastrar_novo_restaurante()`
7. Crie uma docstring para a função `listar_restaurantes()`
8. Crie uma docstring para a função `alternar_estado_restaurante()`
9. Crie uma docstring para a função `escolher_opcao()`
10. Crie uma docstring para a função `main()`

# Exercícios de Python

## Exercícios de Atributos e Métodos de Instância

1. Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
2. Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
3. Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
4. Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
5. Altere o valor do atributo nome para 'Bistrô'.
6. Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
7. Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
8. Mude o estado da instância restaurante_pizza para ativo.
9. Imprima no console o nome e a categoria da instância restaurante_praca.

## Exercícios de Classes e Instâncias

1. Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
2. Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
3. Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
4. Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
5. Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.

## Desafios

1. Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
2. Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
3. Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
4. Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.
5. Crie uma instância da classe e imprima o valor da propriedade titular.
6. Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
7. Crie um método de classe para a conta ClienteBanco.

## Exercícios de Classes e Métodos Estáticos

1. Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.
2. Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.
3. Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.
4. Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.
5. Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.
6. No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.
7. No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.
8. Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro.

## Exercícios de Arquivos e Importação

1. No arquivo `biblioteca.py`, empreste o livro chamando o método `emprestar` e imprima se o livro está disponível ou não após o empréstimo.
2. No arquivo `biblioteca.py`, utilize o método estático `verificar_disponibilidade` para obter a lista de livros disponíveis publicados em um ano específico.
3. Crie um arquivo chamado `main.py`, importe a classe `Livro` e, no arquivo `main.py`, instancie dois objetos da classe `Livro` e exiba a mensagem formatada utilizando o método `str`.

## Exercícios de Herança e Polimorfismo

1. Implemente uma classe chamada `Veiculo` com um construtor que aceita dois parâmetros, `marca` e `modelo`. A classe deve ter um atributo protegido `_ligado` inicializado como `False` por padrão.
2. Adicione um método especial `__str__` à classe `Veiculo` que retorna uma mensagem formatada com a marca, modelo e o estado de ligado/desligado do veículo.
3. Agora, crie uma classe chamada `Carro` que herda da classe `Veiculo`. No construtor da classe `Carro`, inclua um novo atributo chamado `portas` que indica a quantidade de portas do carro.
4. Adicione um método especial `__str__` à classe `Carro` que estenda o método da classe pai (`Veiculo`) e inclua a informação sobre a quantidade de portas do carro.
5. Similarmente, crie uma classe chamada `Moto` que também herda de `Veiculo`. Adicione um novo atributo chamado `tipo` ao construtor, indicando se a moto é esportiva ou casual.
6. Adicione um método especial `__str__` à classe `Moto` que estenda o método da classe pai (`Veiculo`) e inclua a informação sobre o tipo da moto.
7. Crie um arquivo chamado `main.py` no mesmo diretório que suas classes.
8. No arquivo `main.py`, importe as classes `Carro` e `Moto`. Em seguida, crie três instâncias de `Carro` e `Moto` com diferentes marcas, modelos, quantidade de portas e tipos.
9. Para cada instância, imprima no console as informações utilizando o método `__str__`.

## Exercícios de Classes Abstratas

1. Crie uma classe chamada `Veiculo` com um método abstrato chamado `ligar`.
2. No mesmo arquivo, crie um construtor para a classe `Veiculo` que aceita os parâmetros `marca` e `modelo`.
3. Crie uma nova classe chamada `Carro` que herda da classe `Veiculo`.
4. No construtor da classe `Carro`, utilize o método `super()` para chamar o construtor da classe pai e atribua o atributo específico `cor` à classe filha.
5. Em um arquivo chamado `main.py`, importe a classe `Carro`.
6. No arquivo `main.py`, instancie três objetos da classe `Carro` com diferentes características, como `marca`, `modelo` e `cor`.
