import re


class Solution:
    def __init__(self, file_name='input') -> None:
        with open(file_name, 'r') as f:
            self.data = f.read()
        lines = self.data.split('\n')
        self.card_details = self.get_card_details(lines)

    def get_winning_numbers(self, line: str) -> list[int]:
        raw = re.search(r'^Card\s+\d+: (.*)\|.*$', line).group(1)
        winning_numbers = [int(x) for x in raw.split()]
        return winning_numbers

    def get_my_numbers(self, line: str) -> list[int]:
        raw = re.search(r'^.*\| (.*)$', line).group(1)
        my_numbers = [int(x) for x in raw.split()]
        return my_numbers

    def get_card_id(self, line: str) -> int:
        return int(re.findall(r'^Card\s+(\d+).*$', line)[0])

    def get_matches(self, line: str) -> int:
        winning = self.get_winning_numbers(line)
        my = self.get_my_numbers(line)

        count = 0
        for number in winning:
            count += my.count(number)
        return count

    def get_card_details(self, all_lines: list[str]) -> dict:
        card_details = dict()
        for line in all_lines:
            card_details[self.get_card_id(line)] = self.get_matches(line)
        return card_details

    def is_finished(self, values: list) -> bool:
        for value in values:
            if list(value.values())[0] == False:
                return False
        return True

    def generate_copies(self, card_number) -> list:
        r = list(range(card_number + 1, card_number + self.card_details[card_number] + 1))
        max_card = len(self.card_details)
        if card_number + self.card_details[card_number] + 1 > max_card:
            r = list(range(card_number + 1, max_card + 1))
        return [{'id': elem, 'inspected': False} for elem in r]

    def solve(self):
        result = []
        original = [{'id': elem, 'inspected': False} for elem in self.card_details.keys()]
        i = 0
        while True:
            if original[i]['inspected'] == False:
                original += self.generate_copies(original[i]['id'])
                original[i]['inspected'] = True
            i += 1
            try:
                original[i]
            except IndexError:
                break
        print(f'Result: {len(original)}')



if __name__ == "__main__":
    Solution().solve()
