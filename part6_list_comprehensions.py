""" Compreensão de Lista """

""" Com frequência iremos transformar uma lista em outra, 
 escolhendo apenas alguns elementos, transformando tais elementos
 ou ambos. E compreensão de lista é o modo pythonic de se fazer isso."""

""" Uma compreensão de lista é uma construção sintática disponível 
em algumas linguagens de programação para criação de uma lista baseada 
em listas existentes. 
Ela segue a forma da notação de definição de conjunto matemática 
como forma distinta para uso de funções de mapa e filtro """

even_numbers = [x for x in range(5) if x % 2 == 0] #[0, 2, 4]
print(even_numbers)

squares = [x * x for x in range(5)] # [0, 1, 4, 9, 16]
print(squares)

""" é possível transformar dicionários em conjuntos da mesma forma: """

square_dict = { x: x * x for x in range(5) } #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(square_dict)

square_set = { x * x for x in [1, -1] } # { 1 }
print(square_set)

""" Se você não precisar do valor da lista, é comum usar um sublinhado
 como variável:"""

zeroes = [0 for _ in even_numbers] #possui o mesmo tamanho de even_numbers # [0, 0, 0]
print(zeroes)

""" Uma compreensão de lista pode incluir múltiplos for: """

pairs = [(x, y)
         for x in range(10)
         for y in range(10)] # 100 pairs (0,0), (0,1)...(9,8), (9,9)
print(pairs)

""" E os for que vêm depois podem utilizar os resultados dos primeiros: """

increasing_pairs = [(x, y)
                    for x in range(10)
                    for y in range(x + 1, 10)]
print(increasing_pairs)