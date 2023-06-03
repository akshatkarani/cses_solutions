# Two Knights


def count(k: int) -> int:
    k_sq = k * k
    total = (k_sq * (k_sq -1)) / 2
    attack = (k-1) * (k-2) * 2 * 2
    return total - attack 


def solution(n: int) -> str:
    for i in range(1, n + 1):
        c = count(i)
        print(int(c))


def main():
    input_list = input().split()
    solution(int(input_list[0]))


if __name__ == "__main__":
    main()
