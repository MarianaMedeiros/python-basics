""" Controle de fluxo """

""" if/elseif/else padrão... """

if(1>2):
    message = "if only one were greater then two..."
elif(1>3):
    message = "elif stands for 'else if'"
else:
    message = "when all else fails, use else (if you want to!)"

""" ternários: """

x = 5
parity = "even" if x % 2 == 0 else "odd"

""" loop while """

x = 0
while x < 10:
    print(x, " is less than 10")
    x += 1

""" porém o for e in é mais utilizado: """
x = 0
for x in range(10):
    print(x, "is less than 10")

""" ou, com uma lógica mais complexa, pode-se usar continue e break: """

x = 0
for x in range(10):
    if x == 3:
        continue #vai para a próxima iteração imediatamente
    if x == 5:
        break # sai do loop completamente
    print(x)