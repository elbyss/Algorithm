import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
x = int(input())
n = int(input())
ans = 0
for i in range(n):
  a, b = map(int, input().split())
  ans += a*b
if (ans == x):
  print ("Yes")
else:
  print ("No")
  
