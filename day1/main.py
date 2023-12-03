import re


def read_file(file_name="input") -> str:
    with open(file_name, 'r') as f:
        return f.read()


def main():
    data = read_file()
    lines = data.split('\n')
    sum = 0
    for line in lines:
        digits = re.findall(r'[0-9]', line)
        sum += int(f'{digits[0]}{digits[-1]}')

    print('Result: ', sum)


if __name__ == "__main__":
    main()
