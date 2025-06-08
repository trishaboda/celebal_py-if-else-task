# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

n = int(input().strip())
S = input().strip().split()
k = int(input().strip())

a = list(combinations(sorted(S), k))
prob = list(filter(lambda x: 'a' in x, a))

print(len(prob) / len(a))
