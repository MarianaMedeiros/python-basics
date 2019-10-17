""" imports """

import re as regex
import matplotlib as plt
from collections import defaultdict, Counter #importa somente os módulos a serem utilizados e não a biblioteca inteira
my_regex = regex.compile("[0-9]", regex.I)
print(my_regex)

##############################################################

""" Aritmética """

""" No python 2.7 o resultado da divisão é em inteiros. 
portanto, era necessário utilizar um from __future__ import division
Ja no python 3 não temos mais esse problema"""

print("5/2 => " + str(5/2)) #float
print("5//2 => " + str(5//2)) #int

""" Funções """


def double(x):
    """ docstring, que contém a documentação do que a função faz
     ex: essa função retorna o dobro de sua entrada"""
    return x * 2


print(double(4))


""" As funções de python são de primeira classe,
o que significa que podemos atribui-las a variáveis 
e passá-las para as funções como quaisquer outros argumentos:"""


def apply_to_one(f):
    """chama a função f com 1 como seu argumento"""
    return f(1)


my_double = double
x = apply_to_one(my_double)
print(x)


""" pequenas funções anônimas ou lambdas: """

y = apply_to_one(lambda x: x + 4)
print(y)


another_double = lambda x: 2 * x # não faça isso!!!!
def another_double(x): return 2 * x # faça isso! :)

""" os parâmetros das funções podem ter um valor padrão, caso não especificados: """
def my_print(message="my default message"):
    print(message)

my_print("hey!!")
my_print()

""" também é possivel especificar argumentos pelo nome: """

def subtract(a=0, b=0):
    print(a - b)
    return a - b


subtract(10, 5) # 5
subtract(0, 5) # -5
subtract(b=5) #-5


""" String podem ser delimitadas por aspas simples ou duplas 
e usa-se a barra invertida (\) para codificar caracteres especiais.
Por exemplo: """

tab_string = "\t"
print(len(tab_string)) # é 1

""" Para utilizar a própria barra invertida como string mesmo,  
pode-se criar uma string bruta usando r:"""

not_tab_string = r"\t"
print(len(not_tab_string)) # é 2

""" Para Strings múltiplas, usa-se aspas tripas """

multi_line_string = """esta é a primeira linha.
e esta é a segunda
e esta é a terceira =)"""

""" Try Except, para tratamento de exceções (são usadas livremente no Python)"""

try:
    print(0/0)
except ZeroDivisionError:
    print("cannot divide by zero")