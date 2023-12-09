import re
import json


class Solution:
    def __init__(self, file_name='input'):
        with open(file_name, 'r') as f:
            self.data = f.read()
            lines = [line for line in self.data.split('\n') if line]
            self.instructions = lines[0]
            self.map = dict()

            for line in lines[1:]:
                extract = re.findall(r'^(\w{3})\s+=\s+\((\w{3}),\s+(\w{3})\).*$', line)[0]
                neighbours = {
                    'L': extract[1],
                    'R': extract[2]
                }
                self.map[extract[0]] = neighbours
            # print(json.dumps(self.map, indent=2))

    def solve(self):
        current = 'AAA'
        pos = 0
        count = 0
        while current != 'ZZZ':
            current = self.map[current][self.instructions[pos]]
            pos += 1
            count += 1
            if pos >= len(self.instructions):
                pos = 0

        print(f'Result: {count}')
        print(count / len(self.instructions))


if __name__ == "__main__":
    Solution().solve()
