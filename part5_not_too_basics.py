""" Ordenação: """

""" Toda lista de Python possui um método sort que ordena seu espaço.
 Para não bagunçar a lista, podemos usar a função sorted, que retorna uma nova lista:"""

x = [4, 1, 2, 3]
y = sorted(x) # y agora é [1, 2, 3, 4] e o x não foi alterado
x.sort # x agora é [1, 2, 3, 4], foi alterado

""" Por padrão, o sort e o sorted organizam uma lista da menor para a maior 
baseada em uma comparação ingênua de elementos uns com os outros. """

""" Se você quer que os elementos sejam organizados do maior para o menor,
 você pode especificar o parâmetro reverse=True. E, em vez de comparar
 os elementos com eles mesmos, compare os resultados da função que você especificar
 com key: """

# organiza a lista pelo valor absoluto  do maior para o menor
x = sorted([-4, 1, -2, 3], key=abs, reverse=True) # [-4, 3, -2, 1]

#organiza as palavras e contagens da mais alta para a mais baixa
word_counts = {'a':2, 't':1, 'q':0, 'f':1, 'o':4, 'm':2, 'n':0}
print(word_counts)
wc = sorted(word_counts.items(),
            key=lambda count: count[1],
            reverse=True)
print(wc)