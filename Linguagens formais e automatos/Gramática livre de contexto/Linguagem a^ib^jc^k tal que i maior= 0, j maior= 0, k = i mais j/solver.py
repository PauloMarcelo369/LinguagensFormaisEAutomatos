from glc import GLC

def main():
    V = {'S', 'A', 'B'}
    Sigma = {'c', 'a', 'b'}
    R = {
        ('S', 'A'),
        ('S', 'B'),
        ('S', ''),
        ('A', 'aAc'),
        ('A', 'aBc'),
        ('A', 'ac'),
        ('B', 'bBc'),
        ('B', 'bc'),
    }
    start = 'S'
    G = GLC(V,Sigma,R,start)
    G.check()
    teste(G)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


    
