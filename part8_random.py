""" Aleatoriedade """

""" Conforme aprendemos data science, precisaremos gerar números aleatórios
 com uma certa frequência, o que pode ser feito com o módulo random:"""

import random
four_uniform_randoms = [random.random() for _ in range(4)] # random.random() produz numeros uniformemente antes 0 e 1
print(four_uniform_randoms)

""" O módulo random de fato produz numeros pseudoaleatórios (ou seja, deterministicos)
 baseado em um estado interno que você pode configurar com random.seed se quiser obter resultados
 reproduzíveis:"""

random.seed(10) #configura seed para 10
print(random.random())
print(random.random())
print(random.random())
random.seed(10) #configura seed para 10 novamente
print(random.random())
print(random.random())
print(random.random())

""" às vezes usaremos random.randrange, que leva um ou dois argumentos 
e retorna um elemento escolhido aleatoriamente do range() correspondente: """

print(random.randrange(10)) #escolhe aleatoriamente de range(10)
print(random.randrange(10))

print(random.randrange(3, 6)) #escolhe aleatoriamente de range(3,6)
print(random.randrange(3, 6))
print(random.randrange(3, 6))

""" Existem mais alguns métodos que achamos convenientes em certas ocasiões. 
 random.shuffle reordena os elementos de uma lista aleatoriamente: """

up_to_ten = list(range(10))
print(up_to_ten)
random.shuffle(up_to_ten)
print(up_to_ten)

""" Se você precisar escolher um elemento randomicamente de uma lista,
 você pode usar random.choice:"""
random.seed(10)
my_best_friend = random.choice(["Alice","Bob","Charlie"])
print(my_best_friend)

""" E se você precisar escolher aleatoriamente uma amostra dos elementos
 sem substituição (por exemplo, sem duplicatas), você pode usar random.sample:"""
random.seed(2)
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6)
print(winning_numbers)

""" Para escolher uma amostra de elementos com substituição (por exemplo, permitindo duplicatas),
 você pode fazer múltiplas chamadas para random.choice:"""

four_with_replacement = [random.choice(range(10)) for _ in range(4)]
print(four_with_replacement)