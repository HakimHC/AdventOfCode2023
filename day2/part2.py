import re


def read_file(file_name="input") -> str:
    with open(file_name, 'r') as f:
        return f.read()


def add_power_min(line: str):
    count = {
        "red": 0,
        "blue": 0,
        "green": 0
    }
    sets = line.split(';')
    for _set in sets:
        kvs = re.findall(r'(\d+) (\w+),?', _set)
        for kv in kvs:
            if int(kv[0]) > count[kv[1]]:
                count[kv[1]] = int(kv[0])

    print(count)
    res = 1
    for i in count.values():
        res *= i
    print(res)
    return res




def main():
    data = read_file()
    lines = data.split('\n')
    all_power = []
    for line in lines:
        clean_line = re.search(r'^Game \d+: (.*)$', line).group(1)
        all_power.append(add_power_min(clean_line))

    print(all_power)
    print(f'Result: {sum(all_power)}')


if __name__ == "__main__":
    main()
