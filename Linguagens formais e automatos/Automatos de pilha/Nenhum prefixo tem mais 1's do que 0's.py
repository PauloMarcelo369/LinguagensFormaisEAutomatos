from ap import AP

def main():
    Q = {'q1','q2','q3'}
    Sigma = {'1','0'}
    Gamma = {'$','Z'}
    delta = {('q1','0','' ):{('q1','Z')},
         ('q1','1','Z' ):{('q2','' )},
         ('q2','0',''):{('q1','Z' )},
         ('q2','1' ,'$'):{('q3', '' )},
         ('q2','1','Z' ):{('q2','' )}
         }
    q0 = 'q1'
    Z0 = '$'
    F = {'q1', 'q2'}
    M = AP(Q,Sigma,Gamma,delta,q0,Z0, F)
    teste(M)