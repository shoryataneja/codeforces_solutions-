t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    ref = "Timur"

    if sorted(list(ref)) == sorted(list(s)):
        print("Yes")
    else:
        print("No")