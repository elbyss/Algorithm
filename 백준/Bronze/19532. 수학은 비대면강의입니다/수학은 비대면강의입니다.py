import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
a, b, c, d, e, f = map(int, input().strip().split())
for i in range(-999, 1000):
  for j in range(-999, 1000):
    if (a*i + b*j == c) and (d*i + e*j == f):
      print(i, j)
      break