t = int(input())
k = "codeforces"
for i in range(t):
    count = 0
    s = input()
    n = len(s)
    for i in range(n):
        if s[i] != k[i]:
            count += 1 
    print(count)
