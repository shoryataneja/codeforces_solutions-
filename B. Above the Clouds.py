t = int(input())
for _ in range(t):
    n = int(input())
    s = str(input())

    boolean_check = False

    for i in range(1, n - 1):       
        for j in range(i + 1, n):   
            a = s[:i]
            b = s[i:j]
            c = s[j:]
            if b in (a + c):
                boolean_check = True
                break
        if boolean_check:
            break


    if boolean_check == True:
        print("yes")
    else:
        print(("no"))