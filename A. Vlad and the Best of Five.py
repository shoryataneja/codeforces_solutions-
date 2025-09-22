t = int(input())

for _ in range(t):
    s = str(input())
    n = len(s)
    count_a = 0
    count_b = 0 
    for i in s:
        if i == "A":
            count_a += 1 
        else:
            count_b += 1 
    if count_b > count_a:
        print("B")
    else:
        print("A")