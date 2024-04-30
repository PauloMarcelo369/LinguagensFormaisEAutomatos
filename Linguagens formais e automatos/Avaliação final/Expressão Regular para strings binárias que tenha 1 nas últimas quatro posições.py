from regexp import *

def main():

    x = input() 
    #L é o conjunto de palavras no alfabeto {0,1}   
    #cujo  terceiro símbolo da direita para a esquerda é 1.
    # Ex: 100,101,0100,0111, etc
    # E = (0+1)*1(0+1)^2
    
    e1 = Concat(Star(Or(Literal('1'), Literal('0'))), Literal('1'))
    
    e2 = Concat(Concat(Or(Or(Literal('1'), Literal('0')), Epsilon()), Or(Or(Literal('1'), Literal('0')), Epsilon())),  Or(Or(Literal('1'), Literal('0')), Epsilon()))
    e2 = Concat(e1, e2)
    print( e2.matches(x) )  

main()