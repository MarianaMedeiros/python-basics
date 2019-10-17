""" Listas - coleção ordenada -> um array com mais funcionalidades """

integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [integer_list, heterogeneous_list]

list_length = len(integer_list) # 3
list_sum = sum(integer_list) # 6

""" Também é possível configurar o n-ésimo elemento de uma lista com colchetes:  """
x = list(range(10)) # a lista é [0, 1, ..., 9] ||
# precisei converter para lista porque no python 3, a função range retorna um lazy sequence object
zero = x[0]
one = x[1]
nine = x[-1] # é igual a 9, 'Pythonic para o último elemento'
eight = x[-2] # é 8, 'Pythonic' para o anterior ao último elemento
x[0] = -1 # agora a lista é [-1, 1, 2, 3, ..., 9]

""" Também é possível usar colchetes para repartir as listas: """
first_three = x[:3] # [-1, 1, 2]
print(first_three)
three_to_end = x[3:] # [3, 4, ..., 9]
print(three_to_end)
one_to_four = x[1:5] # [1, 2, 3, 4]
print(one_to_four)
last_three = x[-3:] # [7, 8, 9]
print(last_three)
without_first_and_last = x[1:-1] # [1, 2, ... 8]
print(without_first_and_last)
copy_of_x = x[:] #[-1, 1, 2, ..., 9]
print(copy_of_x)

""" O Python possui o operador in para verificar a associação à lista: """
""" Essa verificação pé feita item por item, e deve ser usada somente se a lista for pequena 
- ou não se importe se a verificação for demorar x) """
print(1 in [1, 2, 3]) # Verdadeiro
print(0 in [1, 2, 3]) # Falso

""" Concatenar listas: """

x = [1, 2, 3]
x.extend([4, 5, 6])
print(x)

""" Se quiser manter o valor inicial de x, pode-se usar uma adição na lista """

