t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    sum_list = 0
    for i in range(n):
        count_0 = 0
        count_1 = 0
        for j in range(i, min(i + 300, n)):
            if s[j] == '0':
                count_0 += 1
            else:
                count_1 += 1
            sum_list += max(count_0, count_1)

    print(sum_list)
