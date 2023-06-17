# Number Spiral


def solution(row: int, col: int) -> int:
    max_val = max(row, col)
    upper = max_val**2
    lower = (max_val - 1) ** 2 + 1

    if max_val % 2 == 0:
        if col < row:
            return upper - col + 1
        else:
            return lower + row - 1
    else:
        if col < row:
            return lower + col - 1
        else:
            return upper - row + 1


def main():
    t = int(input())
    outputs = []
    for _ in range(t):
        row, col = map(int, input().split())
        output = solution(row, col)
        outputs.append(output)
    for output in outputs:
        print(output)


if __name__ == "__main__":
    main()
