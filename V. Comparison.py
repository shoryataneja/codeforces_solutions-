a, s, b = input().split()
a = int(a)
b = int(b)

if s == "<" and a < b :
    print("Right")
elif s == ">" and a > b:
    print("Right")
elif s == "=" and a == b:
    print("Right")
else:
    print("Wrong")