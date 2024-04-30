# Strings binárias que começam ou terminam com 01
edges = { (0, '') :  [1, 6],
          (1, '0') : [2], 
          (2, '1') : [3],
          (2, '0') : [10],
          (3, '0') : [4],
          (3, '1') : [10],
          (4, '0') : [5],
          (4, '1') : [10],
          (5, '0') : [10],
          (5, '1') : [10],
          (6, '1') : [7],
          (7, '0') : [8],
          (7, '1') : [10],
          (8, '1') : [9],
          (8, '0') : [10],
          (9, '0') : [10],
          (9, '1') : [10],
          (10, '1') : [10],
          (10, '0') : [10]
          
 }
initial   = 0
accepting = [2, 4, 7, 8, 10] 

def epsilon_nfa(string, current, edges, accepting): 
    #print ("current: " + str(current) + "string: " + string )    
    if string == "":
        return  current in accepting       
    else:
        if (current, '') in edges:
          for next in edges[(current,'')]:
            if epsilon_nfa(string, next, edges, accepting):
                    return True
        c = string[0]
        if (current,c) in edges:
            for next in edges[(current,c)]:
                if epsilon_nfa(string[1:], next, edges, accepting):
                    return True
        
        return False
        

string = input()
print (epsilon_nfa( string , initial, edges, accepting) )      