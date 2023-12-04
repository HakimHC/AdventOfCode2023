import re


class Solution:
    def __init__(self, file_name='input') -> None:
        with open(file_name, 'r') as f:
            self.data = f.read()

    def get_winning_numbers(self, line: str) -> list[int]:
        raw = re.search('^Card\s+\d+: (.*)\|.*$', line).group(1)
        winning_numbers = [int(x) for x in raw.split()]
        return winning_numbers

    def get_my_numbers(self, line: str) -> list[int]:
        raw = re.search('^.*\| (.*)$', line).group(1)
        my_numbers = [int(x) for x in raw.split()]
        return my_numbers


    def solve(self):
        lines = self.data.split('\n')
        result = []
        for line in lines:
            print(line)
            winning_numbers = self.get_winning_numbers(line)
            my_numbers = self.get_my_numbers(line)

            count = 0
            for winning in winning_numbers:
                if not count and my_numbers.count(winning) >= 1:
                    count = 1
                elif count and my_numbers.count(winning) >= 1:
                    count *= 2
            result.append(count)

        print(f'Result: {sum(result)}')


if __name__ == "__main__":
    Solution().solve()