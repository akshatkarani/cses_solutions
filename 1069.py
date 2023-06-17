# Repetitions


def solution(s: str) -> int:
    total_max = 0
    current_max = 0
    prev_char = ""
    for ch in s:
        if ch == prev_char:
            current_max += 1
        else:
            current_max = 1
        total_max = max(total_max, current_max)
        prev_char = ch
    return total_max


def main():
    s = input()
    output = solution(s)
    print(output)


if __name__ == "__main__":
    main()
