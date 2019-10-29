""" Um problema com as listas é que elas podem crescer sem parar facilmente.
 range(1000000) cria uma lista com um milhão de elementos.
 Se você apenas precisa lidar com eles um de cada vez, isso pode ser uma fonte infinita de
  ineficiência (ou esgotamento de memória).
  Se você precisa de poucos valores, calcular todos seria uma perda de tempo.

  Um gerador é algo sobre o qual você pode iterar (geralmente usando for) mas cujos
   valores são produzidos apenas quando necessários (preguiçosamente). """

""" Uma forma de criar geradores é com funções e o operador yield: """

def lazy_range(n):
    """ uma versão preguiçosa de range """
    i = 0
    while i < n:
        yield i
        i += 1

""" O loop a seguir consumirá os valores yield """
#for x in lazy_range(5):
    #print(x)


""" O python geralmente vem com uma função laze_range chamada xrange e, 
em python 3, range é, em si, preguiçoso (lazy). Isso significa que você poderia
 criar uma sequência infinita:"""

def natural_numbers():
    """ retorna 1, 2, 3, ... """
    n = 1
    #while True: comentado caso esse .py seja executado
    while n < 100:
        yield n
        n += 1

import sys

a = range(1, 10000)
print(type(a))
print (sys.getsizeof(a))

""" O outro lado da preguiça é que você somente pode iterar com um gerador uma vez.
 Se você precisar iterar múltiplas vezes, você terá que recriar um gerador todas
 as vezes ou usar uma lista."""

""" Uma segunda forma de criar geradores é usar compreensões de for dentro de parênteses: """

lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)

for x in lazy_evens_below_20:
    print('valor atual:' + str(x))

""" Lembre-se que cada dict possui um método items() que retorna uma lista 
 de seus pares vaores-chave. Veremos com mais frequência o método iteritems(), que
 preguiçosamente yields (chama) os pares de valor-chave um de cada vez conforme iteramos
 sobre ele. """

