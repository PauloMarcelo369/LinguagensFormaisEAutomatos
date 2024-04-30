#Expressão Regular quarto símbolo da direita para a esquerda é 1

from regexp import *

def main():
    str = input()
    E = Concat(Concat(Star(Or(Literal('0'), Literal('1'))),Literal('1')),Or(Or(Literal('01'), Literal('10')), Or(Literal('11'), Literal('00'))))
    print( E.matches(str) )


if __name__ == "__main__":
    main()