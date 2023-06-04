# Coin Piles


def solution(a: int, b: int) -> bool:
    return (
        (2 * a - b) % 3 == 0
        and (2 * b - a) % 3 == 0
        and (2 * a - b) >= 0
        and (2 * b - a) >= 0
    )


def main():
    t = int(input())
    result = []
    for _ in range(t):
        a, b = map(int, input().split())
        result.append(solution(a, b))
    for r in result:
        print("YES" if r else "NO")


if __name__ == "__main__":
    main()
