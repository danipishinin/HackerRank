
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lista = list( dict.fromkeys(arr))
    lista.sort()
    lista.reverse()
    print(lista[1])