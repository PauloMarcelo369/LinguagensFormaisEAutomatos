from glc import GLC

def main():
    V = {'S', 'A', 'B', 'C'}
    Sigma = {'0', '1'}
    R = {
        ('S', '0S'),
        ('S', '1A'),
        ('S', ''),
        ('A', '0S'),
        ('A', '1B'),
        ('A', ''),
        ('B', '0C'),
        ('B', ''),
        ('C', '0C'),
        ('C', '1B'),
        ('C', '')
    }
    start = 'S'
    G = GLC(V,Sigma,R,start)
    G.check()
    teste(G)

