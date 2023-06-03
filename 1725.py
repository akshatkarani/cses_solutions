# Dice Probability

cache = {}


def favorable(n: int, i: int) -> int:
    if (n, i) in cache:
        return cache[(n, i)]

    if n == 1:
        if 1 <= i <= 6:
            return 1
        return 0

    count = 0
    for j in range(1, 7):
        count += favorable(n-1, i-j)

    cache[(n, i)] = count

    return count


def solution(n: int, a: int, b: int) -> str:
    total_favor = 0
    for i in range(a, b+1):
        total_favor += favorable(n, i)
    prob = total_favor / (6**n)
    return format(prob, ".6f")


def main():
    input_list = input().split()
    n, a, b = [int(i.strip()) for i in input_list]
    output = solution(n, a, b)
    print(output)


if __name__ == "__main__":
    main()
