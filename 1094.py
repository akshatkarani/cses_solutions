# Increasing Array


def solution(array: list, length: int) -> int:
    bar = array[0]
    moves = 0
    for i in range(1, length):
        if array[i] < bar:
            moves += bar - array[i]
        bar = max(bar, array[i])
    return moves


def main():
    length = int(input())
    array = list(map(int, input().split()))
    output = solution(array, length)
    print(output)


if __name__ == "__main__":
    main()
