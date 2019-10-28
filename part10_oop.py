""" Programação Orientada a Objeto """

""" O python permite que você  defina classes que encapsulam dados e as funções que as operam.
As usaremos algumas vezes ara tornar o código mais limpo e simples."""

""" Por convenção, damos nomes PascalCase às classes: """

class Set:
    #funções de membro
    #cada uma pega um parâmetro self (outra convenção)
    #que se refere ao objeto set sendo usado em questão


    def __init__(self, values=None):
        """ construtor
        Ele é chamado quando você cria um novo Set"""
        self.dict = {}  # cada instância de Set possui sua própria propriedade dict

        if values is not None:
            for value in values:
                self.add(value)

    def __repr__(self):
        """ essa é a representação da string de um objeto Set
         se você digitá-la no prompt do python ou passá-la para str()"""
        return "Set: " + str(self.dict.keys())

    #Representaremos a associação como uma chave em self.dict com valor True
    def add(self, value):
        self.dict[value] = True

    #valor está no Set se ele for uma chave no dicionário
    def contains(self, value):
        return value in self.dict

    def remove(self, value):
        del self.dict[value]

""" Poderíamos usar desta forma: """
s = Set([1,2,3])
s.add(4)
print(s.contains(4))
s.remove(3)
print(s.contains(3))