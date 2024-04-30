#linguagem definida por ab*ba(ab)*

# Coloque aqui as transições do seu autômato
edges = {
    (0,'a') : 1,
    (1,'b') : 2,
    (2,'b') : 2,
    (2,'a') : 3,
    (3,'a') : 4,
    (4,'b') : 5,
    (5,'a') : 4 
}

#Coloque aqui os estados finais do seu autômato
accepting = [3, 5]  

initial   = 0

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
print(dfa(string, initial, edges, accepting))