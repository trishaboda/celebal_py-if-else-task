# run in python 2
if __name__ == '__main__':
    n = int(raw_input())
    a = tuple(map(int, raw_input().split()))
    print(hash(a))