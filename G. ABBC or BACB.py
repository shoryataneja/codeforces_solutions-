t = int(input())
for _ in range(t):
    k = input()
    s = list(k)
    n = len(s)
    count = 0 
    changed = True
    # val = 0 
    while changed:
        changed = False 
        val = 1 
        while val < n-1:
            for i in range(1,n):
                if s[i] == "B" and s[i-1] == "A":
                    s[i] = "C"
                    s[i-1] = "B"
                    count += 1 
                    changed = True
                    val += 2 
                if s[i] == "A" and s[i-1] == "B":
                    s[i] = "B"
                    s [i-1] = "C"
                    count += 1 
                    changed = True
                    val += 2 
                else:
                    val += 1
    print(count)
