# q = int(input())
# for _ in range(q):
#     a, b, n, S = map(int, input().split())
#     boolean_check = False

#     for i in range(min(a, S // n) + 1):
#         total = i * n
#         if total + min(b, S - total) == S:
#             boolean_check = True
#             break

#     if boolean_check == True:
#         print("YES")
#     else:
#         print("NO")

q = int(input())
for _ in range(q):
    a, b, n, S = map(int, input().split())

    max_n_coins = min(S // n, a)
    total_from_n = max_n_coins * n
    remaining = S - total_from_n

    if remaining <= b:
        print("YES")
    else:
        print("NO")
