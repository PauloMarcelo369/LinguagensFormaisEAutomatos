# Strings binárias que começam ou terminam com 01
edges = { (0, '') :  [1,3,5],
          (0, '0') : [0], 
          (0, '1') : [0,7],
          (1, '1') : [2],
          (2, '0') : [4],
          (2, '1') : [4],
          (3, '1') : [4],
          (4, '0') : [6],       
          (4, '1') : [6],
          (5, '1') : [6],
          (6, '1') : [7],
          (6, '0') : [7]
          
 }
initial   = 0
accepting = [7] 

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