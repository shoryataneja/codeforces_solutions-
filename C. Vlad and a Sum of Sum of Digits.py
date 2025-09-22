MAX_N = 200000
digit_sum = [0] * (MAX_N + 1)


for i in range(1, MAX_N + 1):
    digit_sum[i] = digit_sum[i - 1] + sum(int(d) for d in str(i))

t = int(input())
for _ in range(t):
    n = int(input())
    print(digit_sum[n])