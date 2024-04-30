def main():
    
    (states, edges, initial, final) = eval(input())
    
    states2 = [1,2,3]
    edges2 = {
        (1, '1'): 1, 
        (1, '0'): 2, 
        (2, '0'): 2,
        (2, '1'): 3,
        (3, '1'): 3,
        (3, '0'): 3
    }
    initial2 = 1
    final2 = [1,2]
    
    teste(states2, edges2, initial2, final2) 