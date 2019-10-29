""" Enumeração - enumerate """

""" Com alguma frequência você vai querer iterar por uma lista e usar seus elementos e seus índices """

def do_something(index, value):
    print(str(index) + ' - ' + str(value))

def do_something_2(index):
    print(index)

documents = ['a', 'b', 'c', 'd', 'f']

#não é pythonic
for i in range(len(documents)):
    document = documents[i]
    do_something(i, document)

#também não é pythonic:
i = 0
for document in documents:
    do_something(i, document)
    i += 1

""" A solução Pythonic é enumrate (enumerar), que produz tuplas (index, element): """

for i, document in enumerate(documents):
    do_something(i, document)

""" Da mesma forma, se apenas quisermos os índices: """

for i in range(len(documents)): do_something_2(i) #não é pythonic
for i, _ in enumerate(documents): do_something_2(i) #pythonic

""" Usaremos isso bastante! """