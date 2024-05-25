import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
n = int(input())

def fibonacci(n):
  dp = [0] * (n + 1)
  dp[0] = 0
  dp[1] = 1

  for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

  return dp[n]

print(fibonacci(n))