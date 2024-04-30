#Código Python 
# Automato que aceita string binarias com a substring 01
# 
#   
edges = {
(1, '1') : 2,
(2, '0') : 3,
(2, '1') : 4,
(3, '0') : 5,
(3, '1') : 6,
(4, '0') : 2,
(4, '1') : 3,
(5, '0') : 4,
(5, '1') : 5,
(6, '0') : 6,
(6, '1') : 2   
}

current = 1
accepting = [6]

# Função que roda o autômato
def dfa(string, current, edges, accepting):
    if string == "":
        return current in accepting
    else:
        letter = string[0]
        remainder = string[1:]
        if (current, letter) in edges:
            newstate = edges[(current, letter)]
            return dfa(remainder, newstate, edges, accepting)
        return False


string = input()
print (dfa(string, current, edges, accepting))