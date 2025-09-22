t = int(input())

for _ in range(t):
    s = str(input())
    if s.endswith("us"):
        s = s[:-2] + "i"
    print(s)