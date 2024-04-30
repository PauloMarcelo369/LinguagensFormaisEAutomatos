def nfa(string, current, edges, accepting): 
    if string == "":
        return  current in accepting        
    else:
        c = string[0]
        if (current,c) in edges:
            for next in edges[(current,c)]:
                if nfa(string[1:], next, edges, accepting):
                    return True
        return False

def main():     
    
    string = input()
 
    # Exemplo de NFA que aceita as strings binárias com o penúltimo dígito igual a 1
    edges = {(0,'0') : [1,3, 5],
            (0,'1') : [1,2, 5],
            (0,'2') : [2,3, 5],
            (1,'1') : [1],
            (1,'0') : [1],
            (1,'2') : [5],
            (2,'1') : [2],
            (2,'2') : [2],
            (2,'0') : [5],
            (3,'0') : [3],
            (3,'2') : [3],
            (3,'1') : [5]
    }
    initial   =  0 # estado inicial
    accepting = [5] # conjunto de estado final

    print ( nfa(string, initial, edges, accepting) )

main()