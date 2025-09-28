a,b = map(int,input().split())


def ceil(x):
    if int(x) == x:   
        return int(x)
    elif x > 0:
        return int(x) + 1
    else:
        return int(x)
    

def normal_round(x):
    if x - int(x) >= 0.5:
        return int(x) + 1
    else:
        return int(x)
    

print("floor",a,"/",b,"=",a//b)
print("ceil",a,"/",b,"=",ceil(a/b))
print("round",a,"/",b,"=",normal_round(a/b))