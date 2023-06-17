# Missing Number


def solution(n: int, input_list: list) -> int:
    input_list = set(input_list)
    for i in range(1, n+1):
        if i not in input_list:
            return i


def main():
    n = int(input())
    input_list = map(int, input().split())
    output = solution(n, input_list)
    print(output)


if __name__ == "__main__":
    main()
