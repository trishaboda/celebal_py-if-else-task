# Enter your code here. Read input from STDIN. Print output to STDOUT

def count_elements(n):
    c = 1
    for i in range(len(n)):
        if i == len(n) - 1:
            print((c, int(n[i])), end=" ")
            break
        elif n[i] == n[i + 1]:
            c += 1
        else:
            print((c, int(n[i])), end=" ")
            c = 1  

n = list(input().strip())
count_elements(n)
