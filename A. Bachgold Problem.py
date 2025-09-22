# n = int(input())
# m = 10**6
# p =[True]*(m)
# p[0]=p[1] = False
# for i in range(2,m):
#     if p[i] == True:
#         for j in range(i*i,m,i):
#             p[j] = False
# lst = []
# for i in range(n):
#     if p[i] == True:
#         lst.append(i)
# def max_elements(n, lst):
#     if n == 0:
#         return 0, [] 
#     if n < 0:
#         return float('-inf'), [] 
#     max_count = float('-inf')
#     best_combo = []
#     for num in lst:
#         result_count, result_combo = max_elements(n - num, lst)
#         if result_count != float('-inf') and result_count + 1 > max_count:
#             max_count = result_count + 1
#             best_combo = result_combo + [num]

#     return max_count, best_combo
# count,combo = (max_elements(n,lst))
# print(count)
# print(*combo)


n = int(input())

if n % 2 == 0:
    print(n // 2)
    print("2 " * (n // 2))
else:
    print(1 + (n - 3) // 2)
    print("3 " + "2 " * ((n - 3) // 2))
