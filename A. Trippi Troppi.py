t = int(input())
for i in range(t):
    k = input()
    s = list(k)
    # print(s)
    lst = ["i"] * 1
    lst[0] = s[0]
    n = len(s)
    for i in range(n):
        if s[i] == " ":
            lst.append(s[i+1])
    print(''.join(lst))
 
    
    