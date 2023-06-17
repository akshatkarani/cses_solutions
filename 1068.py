# Weird Algorithm


def solution(n: int) -> list:
    nums = [n]
    while True:
        if n == 1:
            break
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        nums.append(n)
    return nums


def main():
    n = int(input())
    output = solution(n)
    print(" ".join(map(str, output)))


if __name__ == "__main__":
    main()
