# Permutations


def solution(n: int) -> list:
    output = [1, 3, 5, 2, 4]
    if n < 5:
        print("NO SOLUTION")
    else:
        for i in range(6, n + 1):
            if i % 2 == 0:
                output = [i] + output
            else:
                output.append(i)
        print(" ".join(map(str, output)))


def main():
    n = int(input())
    solution(n)


if __name__ == "__main__":
    main()
