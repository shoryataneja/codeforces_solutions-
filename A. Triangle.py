lst = list(map(int,input().split()))
possible = False 
segment = False

for i in range(4):
    for j in range(i+1,4):
        for k in range(j+1,4):
            a, b, c = sorted([lst[i], lst[j], lst[k]])
            if a + b > c:
                possible = True
            elif a + b == c:
                segment = True

if possible:
    print("TRIANGLE")
elif segment:
    print("SEGMENT")
else:
    print("IMPOSSIBLE")