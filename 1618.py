# Trailing Zeros


def solution(n: int) -> int:
    output = 0
    while n > 0:
        n //= 5
        output += n
    return output


def main():
    n = int(input())
    output = solution(n)
    print(output)


if __name__ == "__main__":
    main()
