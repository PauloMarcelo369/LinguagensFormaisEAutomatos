from glc import GLC

def main():
    V = {'S'}
    Sigma = {'a','b'}
    R = {('S','aSbS'),
         ('S','bSaS'),
         ('S', '')
    }
    S = 'S'
    G = GLC(V,Sigma,R,S)
    teste(G)
    
