""" Ferramentas Funcionais """

""" Ao passar as funções, algumas vezes queremos aplicá-las parcialmente
 para criar funções novas. Em um simples exemplo, imagine que temos uma função
 com duas variáveis: """

def exp(base, power):
    return base ** power

""" e queremos usá-la para criar uma função de uma variável two_to_the
 cuja entrada é um power e cuja saída é o resultado de exp(2, power). 
 Podemos, é claro, fazer isso com def, mas pode ser um pouco complicado: """
#def two_to_the(power):
#    return exp(2, power)

""" Uma abordagem diferente é usar functools.partial: """

from functools import partial, reduce
two_to_the = partial(exp, 2) #agora é uma função de uma variável
print(two_to_the(3)) #8

""" Você também pode usar partial para preencher os argumentos que virão
 depois se você especificar seus nomes: """

square_of = partial(exp, power = 2)
print(square_of(3)) #9

""" Começa a ficar bagunçado quando você adiciona argumentos no meio da função,
 portanto tentaremos evitar isso. 
 Ocasionalmente usaremos map, reduce e filter, que fornecem alternativas funcionais
 para as compreensões de lista: """

def double(x):
    return 2 * x

xs = [1, 2, 3, 4]
twice_xs = [double(x) for x in xs] #[2, 4, 6, 8]
twice_xs = map(double, xs) #[2, 4, 6, 8]
list_doubler = partial(map, double) #funcao que duplica a lista
twice_xs = list_doubler(xs) #novamente [2, 4, 6, 8]

""" Você pode usar map com funções de múltiplos argumentos se fornecer
 múltiplas listas: """

def multiply(x, y): return x * y
products = map(multiply, [1,2], [4,5]) # [1*4, 2*5] = [4, 10]

""" Igualmente, filter faz o trabalho de uma compreensão de lista if: """

def is_even(x):
    """ True se x for par, False se x for ímpar """
    return x % 2 == 0

x_evens = [x for x in xs if(is_even(x))] #[2, 4]
print(x_evens)
x_evens = filter(is_even, xs) #igual ao de cima
print(list(filter(is_even, xs)))

list_evener = partial(filter, is_even) #função que filtra a lista
x_evens = list_evener(xs) #novamente [2, 4]
print(list(x_evens))

""" Reduce combina os dois primeiros elementos de uma lista, então esse resultado
 com o terceiro e esse resultado com o quarto, e assim por diante, produzindo um
 único resultado: """

x_product = reduce(multiply, xs) #1 * 2 * 3 * 4 = 24
print(x_product)

list_product = partial(reduce, multiply) #função que reduz uma lista
x_product = list_product(xs) #novamente 24
print(x_product)