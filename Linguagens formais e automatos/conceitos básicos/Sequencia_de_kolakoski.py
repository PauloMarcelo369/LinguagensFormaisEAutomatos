def kolakoski():
    yield 1
    yield 2
    yield 2
    
    gerador = kolakoski()
    next(gerador)
    next(gerador)
    
    n = 1
    
    for seq in gerador:
        for i in range(seq):
            yield n
        n = 3 - n
                
def main():
    n = int(input())
    gerador = kolakoski()
    l = [next(gerador) for _ in range(n)]
    print(l)

if __name__ == "__main__":
    main()