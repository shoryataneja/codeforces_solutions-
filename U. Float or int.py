s = input().strip()
n = float(s)
num = int(n)

if "." in s:
    integer, decimal = s.split(".")
    if int(decimal) == 0:
        print("int", num)
    else:
        print("float", num, "0." + decimal)
else:
    print("int", num)
