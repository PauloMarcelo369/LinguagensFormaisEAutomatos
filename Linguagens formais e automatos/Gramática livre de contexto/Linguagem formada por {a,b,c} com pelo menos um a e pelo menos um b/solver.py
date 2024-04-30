from glc import GLC

def main():
    V = {'S', 'A', 'B', 'Z'}
    Sigma = {'a','b', 'c'}
    R = {
        ('S', 'cS'),
        ('S', 'aA'),
        ('S', 'bB'),
        ('A', 'cA'),
        ('A', 'aA'),
        ('A', 'bZ'),
        ('B', 'cB'),
        ('B', 'bB'),
        ('B', 'aZ'),
        ('Z', 'aZ'),
        ('Z', 'bZ'),
        ('Z', 'cZ'),
        ('Z', '')
    }
    start = 'S'
    G = GLC(V,Sigma,R,start)
    G.check()
    teste(G)
    
