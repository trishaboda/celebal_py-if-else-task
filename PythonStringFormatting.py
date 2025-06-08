def print_formatted(number):
    # your code goes here
    for i in range(1, number+1):
        s = len(bin(number)[2:])
        print(f"{i:>{s}} {i:>{s}o} {i:>{s}X} {i:>{s}b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)