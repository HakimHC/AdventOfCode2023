import re


MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def get_id(line: str) -> int:
    return re.search(r'^Game (\d+)', line).group(1)


def read_file(file_name="input") -> str:
    with open(file_name, 'r') as f:
        return f.read()


def validate(line: str):
    sets = line.split(';')
    for _set in sets:
        count = {
            "red": 0,
            "blue": 0,
            "green": 0
        }
        kvs = re.findall(r'(\d+) (\w+),?', _set)
        for kv in kvs:
            count[kv[1]] += int(kv[0])

        for key in count:
            if key == 'red' and count[key] > MAX_RED:
                raise ValueError()
            if key == 'green' and count[key] > MAX_GREEN:
                raise ValueError()
            if key == 'blue' and count[key] > MAX_BLUE:
                raise ValueError()



def main():
    data = read_file()
    lines = data.split('\n')
    valid_games = []
    for line in lines:
        game_id = get_id(line)
        clean_line = re.search(r'^Game \d+: (.*)$', line).group(1)
        try:
            validate(clean_line)
            valid_games.append(game_id)
        except ValueError:
            continue

    print(f'Result: {sum([int(i) for i in valid_games])}')


if __name__ == "__main__":
    main()
