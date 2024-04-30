def prefixo(x, y):
    ## Coloque seu código aqui
    if x == "": ## retorna true se a string for vazia
        return True
    elif y == "": ## se for vazia então eu retorno false
        return False
    elif x[0] == y[0]: ## verifica se o primeiro char de x é igual ao de y
        return prefixo(x[1:], y[1:]) ## caso sim, chama a função passando as substrings x[1:], y[1:]
    else:
        return False ##Nain

def main():
    x = input()
    y = input()
    print( prefixo(x,y) )


if __name__ == "__main__":
    main()