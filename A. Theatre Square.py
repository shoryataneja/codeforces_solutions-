import math
n,m,a = map(int,input().split())
leng = math.ceil(n / a)
widt= math.ceil(m / a)
total = leng * widt
print(total)