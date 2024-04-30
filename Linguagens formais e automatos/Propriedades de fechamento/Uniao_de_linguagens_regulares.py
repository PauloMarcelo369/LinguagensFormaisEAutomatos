def main():
    
    sigma = eval(input())
    (states1, edges1, initial1, final1) = eval(input())
    (states2, edges2, initial2, final2) = eval(input())
    
    #adicionando um par ordenado relacionando
    #os dois autômatos 
    states3 = [(1,1), (1,2), (2,1), (2,2), (3,1), (3,2)]
    for x in states1:
        for y in states2:
            states3.append( (x,y) )
    
    
    edges3 = {}
    edges3[ ((1,1), '0')] = (2,2)
    edges3[ ((1,1), '1')] = (1,1)
    edges3[ ((1,2), '0')] = (2,1)
    edges3[ ((1,2), '1')] = (1,2)
    edges3[ ((2,1), '0')] = (2,2)
    edges3[ ((2,1), '1')] = (3,1)
    edges3[ ((2,2), '0')] = (2,1)
    edges3[ ((2,2), '1')] = (3,2)
    edges3[ ((3,1), '0')] = (3,1)
    edges3[ ((3,1), '1')] = (3,1)
    edges3[ ((3,2), '0')] = (3,1)
    edges3[ ((3,2), '1')] = (3,2)
    
    
    final3 = [(1,1), (2,1), (3,1), (3,2)]
    for x in final1:
        for y in final2:
            final3.append( (x,y) )
    
    initial3 = (initial1, initial2)
    
    teste(states3, edges3, initial3, final3)             


