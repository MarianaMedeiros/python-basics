""" args e kwargs """

""" Digamos que queremos criar uma função de ordem alta que tem como entrada
 uma função f e retorna uma função nova que retorna duas vezes o valor de f
 para qualquer entrada: """

def doubler(f):
    def g(x):
        return 2 * f(x)
    return g

""" isto funciona em alguns casos: """
def f1(x):
    return x + 1

g = doubler(f1)

print(g(3)) # 8 ( == (3 + 1) * 2 )
print(g(-1)) # 0 ( == (-1 + 1) * 2 )

""" No entando, ele falha com funções que possuem mais de um único argumento: """

def f2(x, y):
    return x + y

g = doubler(f2)
#print(g(1,2)) #TypeError: g() pega exatamente 1 argumento (2 dados)

""" O que precisamos é de alguma maneira de especificar uma função que leva argumentos
 arbitrários. Podemos fazer isso com a descompactação de argumentos e um pouco de mágica:"""

def magic(*args, **kwargs):
    print("unnamed args: ", args)
    print("keyword args: ", kwargs)

magic(1, 2, key="word", key2="word2")

#imprime:
# unnamed args:  (1, 2)
# keyword args:  {'key': 'word', 'key2': 'word2'}


""" Ou seja, quando definimos uma função como essa, args é uma tupla dos seus argumentos sem nome
 e kwargs é um dict dos seus argumentos com nome. Funciona da forma contrária também, se você quiser
 usar uma list (ou tuple) e dict para fornecer argumentos para uma função: """

def other_way_magic(x, y, z):
    return x + y + z

x_y_list = [1, 2]
z_dict = {"z": 3}

print(other_way_magic(*x_y_list, **z_dict)) # 6

""" Você poderia fazer todos os tipos de truques com isso; apenas usaremos para produzir outras funçẽs
 de ordem alta cujas entradas podem aceitar argumentos arbitrários: """

def doubler_correct(f):
    """ funciona, não importa que tipo de entradas f espera =) """
    def g(*args, **kwargs):
        """ quaisquer argumentos com os quais g é fornecido, os passa para f """
        return 2 * f(*args, **kwargs)
    return g

g = doubler_correct(f2)
print(g(1, 2)) # 6