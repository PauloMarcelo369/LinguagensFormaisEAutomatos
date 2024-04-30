# Expressão Regular {a^mb^n| m+n é par}

from regexp import *

def main():
    str = input()
    E = Or(Concat(Star(Literal('aa')), Star(Literal('bb'))), Concat(Concat(Star(Literal('aa')), Literal('a')), Concat(Star(Literal('bb')), Literal('b'))))
    print( E.matches(str) )


if __name__ == "__main__":
    main()