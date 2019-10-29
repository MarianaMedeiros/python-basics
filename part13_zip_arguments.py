""" Descompactação de Zip e Argumentos """

""" Com uma certa frequência, precisaremos zip (compactar) duas ou mais listas juntas.
 zip transforma listas múltiplas em uma única lista de tuplas de elementos correspondentes:"""

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
zipList = zip(list1, list2) # é [('a', 1), ('b', 2), ('c', 3)]
zipList = list(zipList)
print(zipList)

""" Se as listas são de tamanhos diferentes, zip para assim que a primeira lista acaba.
 Você também pode descompactar uma lista usando um truque curioso: """

pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)

print(letters)
print(numbers)

""" O asterisco desempenha a DESCOMPACTAÇÃO de argumentos, que usa os elementos de pairs
 como argumentos individuais para zip. Dá no mesmo se você chamasse: """

zipExample = zip(('a', 1), ('b', 2), ('c', 3))

""" que retorna [('a', 'b', 'c'), (1, 2, 3)]. """

print(list(zipExample))

""" Você pode usar a descompactação de argumentos com qualquer função: """

def add(a, b): return a + b

add(1, 2) #retorna 3
add([1, 2]) #TypeError!
add(*[1,2]) #retorna 3

""" É raro acharmos isso útil, mas quanto fazemos, é um truque engenhoso """