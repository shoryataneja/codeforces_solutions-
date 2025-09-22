t = int(input())

for _ in range(t):
    n = int(input())
    digit_2 = n % 10
    digit_1 = n//10 
    print(digit_1+digit_2)