from glc import GLC

def main():
    V = {'S', 'X', 'Y', 'Z'}
    Sigma = {'a', 'b'}
    R = {
        ('S','aSbb'),
        ('S','X'),
        ('X','aXb'),
        ('X','Y'),
        ('Y','aYbb'),
        ('Y','Z'),
        ('Z','aZb'),
        ('Z', '')
    }
    start = 'S'
    G = GLC(V,Sigma,R,start)
    G.check()
    teste(G)
    
    
    
    
