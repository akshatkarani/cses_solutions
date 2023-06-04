# Two Sets


def solution(n: int):
    if n % 4 == 0 or n % 4 == 3:
        x, y = [], []
        i = 1
        if n % 4 == 3:
            i = 4
            x, y = [3], [1, 2]
        flag = 1
        while i <= n:
            if flag:
                x.append(i)
                i += 1
                y.append(i)
            else:
                y.append(i)
                i += 1
                x.append(i)
            i += 1
            flag = 1 - flag
        print("YES")
        print(len(x))
        print(*x)
        print(len(y))
        print(*y)

    else:
        print("NO")


def main():
    n = int(input())
    solution(n)


if __name__ == "__main__":
    main()
