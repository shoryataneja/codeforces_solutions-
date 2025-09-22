t = int(input())
count_of_q = 0 

for _ in range(t):
    arr = list(map(int,input().split(" ")))
    count_of_1 = 0 

    for i in arr:
        if i == 1:
            count_of_1 += 1 
    if count_of_1 > 1 :
        count_of_q += 1 
print(count_of_q)


# n = int(input())
# lst = []
# for i in range(n):
#     arr = list(map(int,input().split(" ")))
#     lst.append(arr)
# count = 0 
# for i in lst:
#     for j in i:
#         if j == 1:
#             count += 1
# if count % 2 == 0:
#     print((count//2)-1)
# else:
#     print(count//2)
        


