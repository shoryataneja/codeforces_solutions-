t = int(input())

for _ in range(t):
    s = str(input())

    i = 0
    f_n = 0 
    while i < 3:
        f_n += int(s[i])
        i += 1 

    j = 3
    l_n = 0 
    while j < 6:
        l_n += int(s[j])
        j += 1 
        
    if l_n == f_n:
        print("yes")
    else:
        print("no")