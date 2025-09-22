# n = int(input())

# def fibo(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
    
# print(fibo(n))
n = int(input())
memo={}
def fibo(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

print(fibo(n))