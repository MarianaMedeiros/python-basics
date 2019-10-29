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

x = [1, 2, 3]
y = x + [4, 5, 6]
print(x)
print(y)

""" Mas com mais frequência, anexamos um item de cada vez: """

x = [1, 2, 3]
x.append(0) # x é [1, 2, 3, 0]
y = x[-1] # é 0
z = len(x) # é 4

""" Também pode ser útil desfazer listas, mas a quantidade de elementos 
dos dois lados deve ser a mesma, ou dará um ValueError: """
x, y = [1, 2] # x é 1, y é 2

""" Também podemos usar o underline para um valor que não iremos utilizar: """

_, y = [1,2] # y é 2, o primeiro elemento foi descartado

""" Tuplas - Tudo o que se faz com uma lista (com exceção de modificá-la), é possível fazer em uma tupla 
E a espacificamos através dos parênteses ou nada, em vez de colchete:"""
my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4
my_list[1] = 3

try:
    my_tuple[1] = 3
except TypeError:
        print("cannot modify a tuple")

""" As tuplas são eficazes para retornar múltiplos valores a partir de funções: """
def sum_and_product(x, y):
    return (x + y), (x * y)

sp = sum_and_product(2, 3) # é igual a (5, 6)

s, p = sum_and_product(5, 10) # s = 5, p = 10

""" As tuplas e listas podem ser usadas ara atribuições múltiplas: """
x, y = 1, 2
x, y = y, x

""" Dicionários - estrutura que associa valores com chaves:"""
empty_dict = {} #pythonic
empty_dict2 = dict(); #não tão pythonic assim
grades = { "Joel": 80, "Tim": 95 } #dicionario literal

""" Usa-se colchetes para procurar um valor de ums chave: """
joels_grade = grades["Joel"] # é 80

""" Ao informar uma chave que não existe, retorna um keyError: """
try:
    kates_grade = grades["Kate"]
except KeyError:
    print("no grade for Kate!!")


""" É possível verificar a existência de yma chave com in: """
joel_has_grade = "Joel" in grades #true
kate_has_grade = "Kate" in grades #false

""" Os dicionários possuem o método get que retorna um valor padrão em vez de uma exceção
 quando selecionar uma chave inexistente:"""
joels_grade = grades.get("Joel", 0) #retorna 80
kates_grade = grades.get("Kate", 0) #retorna 0
no_ones_grade = grades.get("No One") #retorna None, que é o padrão do padrão x)

""" Atribuimos pares de valor-chave utilizando colchetes também: """
grades["Tim"] = 99 #substitui o valor antigo
grades["Kate"] = 100 #adiciona um novo registro ao dicionario
num_students = len(grades)
print(num_students)

""" Frequentemente usa-se dicionários para representar dados estruturados: """
tweet = {
    "user": "joelgrus",
    "text": "Data Sciente is awesome",
    "retweet_count": 100,
    "hashtags": ["data", "science", "datascience", "awesome", "yolo"]
}

""" Também podemos ver todas as chaves: """
tweet_keys = tweet.keys() #lista de chaves
print("Tweet Keys: " + str(tweet_keys))

tweet_values = tweet.values() #lista de valores
print("Tweet Values: " + str(tweet_values))

tweet_items = tweet.items() #Lista de chaves-valores
print("Tweet Items: " + str(tweet_items))

"user" in tweet_keys # TRUE MAS É MAIS LENTO PORQUE USA list in
"user" in tweet #TRUE, É MAIS RÁPIDO PORQUE USA dict in E É MAIS PYTHONIC
"joelgrus" in tweet_values #Verdadeiro

""" As chaves dos dicionários devem ser imutáveis. 
Particularmente não se deve usar listas como chaves. 
Se for preciso utilizar uma chave mutipart, é recomendado usar uma tupla 
OU arranjar uma forma de converter essa chave em String."""

""" defaultdict """

""" Exemplo com contagem de palavras em um texto: """
document = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " \
           "Fusce id leo dolor. Fusce porttitor justo luctus, " \
           "ultricies est ut, auctor lacus. Maecenas non auctor leo. " \
           "Aenean iaculis, eros in pharetra accumsan, odio elit sodales odio, " \
           "a faucibus lectus nibh vitae sapien. Pellentesque rutrum ante " \
           "nec metus imperdiet, quis facilisis dolor pellentesque. " \
           "Aenean iaculis et lacus quis aliquam. Nullam vitae lectus sed " \
           "arcu interdum feugiat at posuere velit. Etiam ut varius enim. " \
           "Suspendisse rhoncus, risus a pharetra accumsan, mi odio ornare tellus, " \
           "cursus imperdiet mi lectus ac tortor. Vivamus a venenatis magna. " \
           "Quisque commodo justo nec rhoncus blandit. " \
           "Cras quis libero eu dui congue dictum"

word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts.items())

""" mesma coisa, só que usando except: """

word_counts = {}
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1

""" mesma coisa com get """
word_counts = {}
for word in document:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1

""" defaultdict é como um dicionário comum, só que quando se pesquisa por uma chave inexistente, 
 ele adiciona um valor a ela de argumento zero que for definido:"""

from collections import defaultdict
word_counts = defaultdict(int) #int() produz zero como valor inicial
for word in document:
    word_counts[word] += 1

""" combinando defaultdicts com lists e dicts: """

dd_list = defaultdict(list) #gera uma lista vazia
print(dd_list)

dd_list[2].append(1)
print(dd_list)

dd_dict = defaultdict(dict) #produz um dict vazio
print(dd_dict)

dd_dict["Joel"]["City"] = "Seattle"
print(dd_dict)

dd_pair = defaultdict(lambda: [0,0])
print(dd_pair)

dd_pair[2][1] = 1
print(dd_pair)

""" Contadores - Um counter transforma uma sequência de valores 
em algo parecido com o objeto defaultdict(int), mapeando as chaves
 para as contagens."""

""" COmeçamos pelo histograma: """
from collections import Counter
c = Counter([0, 1, 2, 0]) # c equivale a { 0:2, 1:1, 2:1 }

""" Logo, para simplificar o word_counts: """
word_counts = Counter(document)

""" uma instância do Counter possui um método most_common: """
#imprime as 10 palavras (nesse caso letras) mais usadas e suas quantidades:
print(word_counts.most_common(10))

for word, count in word_counts.most_common(10):
    print(word, count)


""" Conjuntos - set - representa uma coleção de elementos DISTINTOS """

s = set()
s.add(1) # { 1 }
s.add(2) # { 1, 2 }
s.add(2) # ainda { 1, 2 }
x = len(s) #2
y = 2 in s #true
z = 3 in s #false

""" Usaremos os conjuntos por duas razões principais: o in é uma operação muito rápida em conjuntos.
 Com uma grande coleção de itens para usar em um teste de sociedade, 
 um conjunto é mais adequado do que uma lista: """

hundreds_of_other_words = ["with", "of", "in", "etc"]
stopwords_list = ["a", "an", "at"] + hundreds_of_other_words + ["yet", "you"]
"zip" in stopwords_list #false, mas ele verifica todos os elementos - demorado

stopwords_set = set(stopwords_list)
"zip" in stopwords_set #mais rápido!

""" a segunda razão é encontrar os itens distintos em uma coleção: """
item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list) #6
item_set = set(item_list) # {1, 2, 3}
num_distinct_items = len(item_set) #3
distinct_item_list = list(item_set) # [1, 2, 3]

""" usaremos sets com menos frequência do que dicts e lists """