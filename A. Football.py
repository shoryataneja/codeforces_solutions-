# n = input()

# count_0 = 1
# for i in range(len(n)-1):
#     if n[i] == "0" and n[i-1] == "0":
#         count_0 += 1 
    
# count_1 = 1
# for i in range(1,len(n)-1):
#     if n[i] == "1" and n[i-1] == "1":
#         count_1 += 1 

# if count_0 >=7 or count_1 >=7:
#     print("YES")
# else:
#     print("NO")

s = input()

if '0000000' in s or '1111111' in s:
    print("YES")
else:
    print("NO")
