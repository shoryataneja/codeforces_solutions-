t = int(input())

for _ in range(t):
    alpha = list(input())
    word = list(input())
    
    ans = 0 

    for i in range(1,len(word)):
        p_i = alpha.index(word[i-1])
        c_i = alpha.index(word[i])
        ans += abs(c_i-p_i)
    print(ans)