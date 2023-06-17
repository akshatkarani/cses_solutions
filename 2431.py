# Digit Queries

"""
1-9     1 digit
10-99   2 digit
100-999 3 digit

200
200 - 9 = 191
191 - 180 = 11
11 -

100 101 102 103 104 105 106

# l = (digit, start, end)
"""


def solution(n: int) -> int:
    d = 1
    s = 1
    e = 9
    while True:        
        if n > (e - s + 1) * d:
            n -= (e - s + 1) * d
        else:
            n -= 1
            quotient, remainder = divmod(n, d)
            num = s + quotient
            return int(str(num)[remainder])

        s = 10 * s
        e = 10 * s - 1
        d += 1


def main():
    t = int(input())
    outputs = []
    for _ in range(t):
        n = int(input())
        output = solution(n)
        outputs.append(output)
    for output in outputs:
        print(output)


if __name__ == "__main__":
    main()
