#Conjunto de palavras com no máximo um par de 1's consecutivos

from regexp import *

def main():
    str = input()
    E = Or( Concat(Star(Or(Literal('0'), Literal('10') )), Or(Literal('1'), Epsilon())),   Concat(Concat(Star(Or(Literal('0'), Literal('10') )), Literal('11')), Star(Or(Literal('0'), Literal('01')))) )
    print( E.matches(str) )


if __name__ == "__main__":
    main()