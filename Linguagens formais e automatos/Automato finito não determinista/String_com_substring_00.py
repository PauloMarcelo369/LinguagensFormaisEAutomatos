# Exemplo de NFA que aceita as strings binárias com o penúltimo dígito igual a 1
edges = {  (0,'0') : [1],
           (0,'1') : [0,3],
           (1,'0') : [2],
           (1,'1') : [3],
           (2, '1') : [2],
           (2, '0') : [2],
           (3,'1') : [3],
           (3,'0') : [1,4],
           (4, '0') : [2],
           (4, '1') : [3]
           
           
        #   q0 -> 1 : {q0, q3}
        #   q0 -> 0 : {q1}
        #     q1 -> 0 : {q2}
        #     q1 -> 1 : {q3}
        #     *q2 -> 0 : {q2}
        #     *q2 -> 1 : {q1}
        #     q3 -> 1 : {q3}
        #     q3 -> 0 : {q1, q4}
        #     q4 -> 1 : {q3}
        #     q4 -> 0 : {q2}

  
           
}
initial   =  0 # estado inicial
accepting = [2] # conjunto de estado final

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
        

string = input()
print ( nfa(string, initial, edges, accepting) )