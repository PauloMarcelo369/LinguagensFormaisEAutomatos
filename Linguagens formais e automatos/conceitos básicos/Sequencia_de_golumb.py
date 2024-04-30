def golumb():
    yield 1
    yield 2
    yield 2

    freq = {1: 1, 2: 2}
    val = 3
    
    while True:
        freq[val] = freq[val - freq[freq[val-1]]] + 1 if freq[val-1] in freq else 1
        for i in range(freq[val]):
            yield val
        val += 1

def main():
    n = int(input())
    gerador = golumb()
    l = [next(gerador) for i in range(n)]
    print('[{}]'.format(', '.join(map(str, l))))
    
if __name__ == "__main__":
    main()
