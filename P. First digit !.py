n = int(input())

l = len(str(n))

d = 10**(l-1)
# print(d)
f_d = n//d

if f_d % 2 == 0:
    print("EVEN")
else:
    print("ODD")