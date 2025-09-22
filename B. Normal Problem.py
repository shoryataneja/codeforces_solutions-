t = int(input())

for _ in range(t):
    s = str(input())
    ans = ""
    for i in s:
        if i == "q":
            ans += "p" 
        if i == "p":
            ans += "q" 
        if i == "w":
            ans += "w"
    print (ans[::-1])