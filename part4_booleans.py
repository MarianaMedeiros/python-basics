""" Veracidade """

""" Valores booleanos em python são iguais em qualquer linguagem, mas sempre começam com letra maiúscula """

one_is_less_than_two = 1 < 2 #True
true_equals_false = True == False #False

""" O python usa None para indicar um valor não-existente. É como o "null" em outras linguagens """
x = None
print(x == None) #True (mas não é pythonic)
print x is None #True e é pythonic

""" O python permite atribuirmos qualquel valor esperado por um booleano. """
""" Todos os exemplos a seguir são 'Falsos': """

# False
# None
# [] (uma list vazia)
# {} (um dict vazio)
# ""
# set()
# 0
# 0.0

""" Quase todo o restante pode ser tratado como True. Desta forma, 
podemos usar declarações if para testar listas, strings ou dicionários vazios etc...
Porém, às vezes isso pode causar alguns pequenos bugs se você estiver esperando
por este comportamento:"""

def some_function_that_returns_a_string():
    return 'oie'

s = some_function_that_returns_a_string()
if s:
    first_char = s[0]
else:
    first_char = ""

""" Uma forma mais simples de fazer o mesmo: """
first_char = s and s[0]

""" Já que 'and' retorna seu segundo valor quando o primeiro é 'verdadeiro', 
ou o primeiro valor quando não é. Da mesma forma, se x é um número ou,
possivelmente, None, definitivamente é um numero: """

safe_x = x or 0

""" O python possui uma função all que pega uma lista e retorna True precisamente
quando todos os elementos forem verdadeiros, e uma função any, que retorna True 
quando pelo menos um elemento é verdadeiro: """

all([True, 1, {3}]) # True
all([True, 1, {}]) # False
any([True, 1, {}]) # True
all([]) # True - pois não há elementos falsos na lista
any([]) # False - pois não há elementos verdadeiros na lista