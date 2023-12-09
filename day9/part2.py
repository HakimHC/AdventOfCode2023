class Solution:
    def __init__(self, file_name='input'):
        with open(file_name, 'r') as f:
            self.data = f.read()
        lines = self.data.split('\n')
        self.records = list()
        for line in lines:
            self.records.append([int(x) for x in line.split()])

    @staticmethod
    def generate_difference(numbers: list[int]) -> list[int]:
        res = []
        for i in range(1, len(numbers)):
            res.append(numbers[i] - numbers[i - 1])
        return res

    @staticmethod
    def is_all_zeroes(numbers: list[int]) -> bool:
        return not bool([x for x in numbers if x])

    def get_missing_number(self, numbers: list[int]):
        all_list = []
        tmp = numbers
        while not Solution.is_all_zeroes(tmp):
            all_list.append(tmp)
            tmp = Solution.generate_difference(tmp)
        all_list.reverse()
        curr = 0
        for seq in all_list:
            curr = seq[0] - curr
        return curr

    def solve(self):
        res = 0
        for record in self.records:
            res += self.get_missing_number(record)

        print(f'Result: {res}')


if __name__ == "__main__":
    Solution().solve()
