t = int(input())

for _ in range(t):
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))

    option1 = abs(s - arr[0]) + (arr[-1] - arr[0])
    option2 = abs(s - arr[-1]) + (arr[-1] - arr[0])

    total_steps = min(option1, option2)
    print(total_steps)