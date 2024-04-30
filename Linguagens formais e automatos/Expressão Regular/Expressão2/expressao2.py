#Expressão Regular exceto epsilon, 01 e 001
from regexp import *

def main():
    str = input()
    E = Or(
    Or(
        Concat(Literal('1'), Star(Or(Literal('0'), Literal('1')))),
        Concat(
            Concat(Literal('01'), Or(Literal('1'), Literal('0'))),
            Star(Or(Literal('1'), Literal('0')))
        )
    ),
    Or(
        Concat(Literal('0'), Star(Literal('0'))),
        Concat(
            Concat(Literal('00'), Or(Literal('1'), Literal('0'))),
            Concat(
                Or(Literal('0'), Literal('1')),
                Star(Or(Literal('0'), Literal('1')))
            )
        )
    )
)

    
    print( E.matches(str) )


if __name__ == "__main__":
    main()