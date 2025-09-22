n = int(input())

def recursion(year):
    return len(str(year)) == len(set(str(year)))

n += 1 
while not recursion(n):
    n += 1 

print(n)