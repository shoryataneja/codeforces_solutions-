# def fibo(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     return fibo(n-1) + fibo(n-2)

# n = int(input())
# for i in range(1,n+1):
#     print(fibo(i),end=' ')


n = int(input())
a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
