# t = int(input())

# for _ in range(t):
#     n = int(input())
#     vanya = False 
#     for i in range(10):
#         if vanya == False:
#             n += 1 
#             if n % 3 == 0:
#                 vanya = True
#                 break
#         else:
#             n -= 1 
#             if n % 3 == 0:
#                 vanya = True 
#     if vanya == True:
#         print("First")
#     else:
#         print("Second")

t = int(input())
for _ in range(t):
    n = int(input())
    if n%3 != 0:
        print("First")
    else:
        print("Second")



