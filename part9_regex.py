""" Expressões Regulares """

""" As expressões regulares fornecem uma maneira de procurar por texto. 
 São incrivelmente úteis mas um pouco complicadas, tanto que até existem livros sobre elas.
 Alguns exemplos de como usá-las em Python:"""

import re
print(all([ #todas são verdadeiras
    not re.match("a", "cat"), #cat não começa com 'a'
    re.search("a", "cat"), # 'cat' possui um 'a'
    not re.search("c", "dog"), # 'dog' não possui um 'c'
    3 == len(re.split("[ab]", "carbs")), # divide em a ou b para ['c','r','s']
    "R-D-" == re.sub("[0-9]", "-", "R2D2") # substitui dígitos por traços
])) #por isso imprime True

""" individualmente, cada um: """
print("1-)")
print(not re.match("a", "cat"))

print("2-)")
print(re.search("a", "cat"))

print("3-)")
print(not re.search("c", "dog"))

print("4-)")
print(len(re.split("[ab]", "carbs")))
print(re.split("[ab]", "carbs"))
print(3 == len(re.split("[ab]", "carbs")))

print("5-)")
print(re.sub("[0-9]", "-", "R2D2"))
print("R-D-" == re.sub("[0-9]", "-", "R2D2"))