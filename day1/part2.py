import re


def read_file(file_name="input") -> str:
    with open(file_name, 'r') as f:
        return f.read()


def convert(s: str) -> int:
    _map = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    if s in _map:
        return int(_map[s])
    return int(s)


def main():
    data = read_file()
    lines = data.split('\n')
    sum = 0
    for line in lines:
        digits = re.findall(r'(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))', line)
        digits = [convert(digit) for digit in digits]
        sum += int(str(digits[0]) + str(digits[-1]))

    print(f'Result: {sum}')


if __name__ == "__main__":
    main()
