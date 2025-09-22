def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    total_sum = 0
    cnt = 0

    for i in range(n):
        if arr[i] < 0:
            cnt += 1
            arr[i] = -arr[i]
        total_sum += arr[i]

    arr.sort()

    if cnt % 2 == 1:
        total_sum -= 2 * arr[0]

    print(total_sum)


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
