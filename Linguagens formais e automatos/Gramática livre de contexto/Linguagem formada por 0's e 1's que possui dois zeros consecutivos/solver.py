from glc import GLC

def main():
    V = {'S', 'A', 'Z'}
    Sigma = {'0', '1'}
    R = {('S', '0A'), 
         ('S', '1S'),
         ('A', '0Z'),
         ('A', '1S'),
         ('Z', '0Z'),
         ('Z', '1Z'),
         ('Z', '')
    }
    start = 'S'
    G = GLC(V,Sigma,R,start)
    G.check()
    teste(G)
    
