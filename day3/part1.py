class Solution:
    def __init__(self, file_name='input') -> None:
        with open(file_name, 'r') as f:
            self.data = f.read()
        self.matrix = [list(elem) for elem in self.data.split('\n')]
        self.x, self.y = len(self.matrix), len(self.matrix[0])

    @staticmethod
    def is_symbol(char: str) -> bool:
        return not char.isdigit() and (char != '.')

    def is_in_bounds(self, x, y):
        x_range = [i for i in range(self.x)]
        y_range = [i for i in range(self.y)]
        return x in x_range and y in y_range

    def get_numbers(self, x, y):
        if not self.is_in_bounds(x, y):
            raise IndexError
        if self.matrix[x][y] == '.':
            return 0
        idx_left = y
        idx_right = y
        while idx_left > 0 and self.matrix[x][idx_left].isdigit():
            idx_left -= 1
            if not self.matrix[x][idx_left].isdigit():
                idx_left += 1
                break
        while idx_right < self.y and self.matrix[x][idx_right].isdigit():
            idx_right += 1
        res = int(''.join(self.matrix[x][idx_left:idx_right]))
        for i in range(idx_left, idx_right):
            self.matrix[x][i] = '.'
        return res

    def solve(self):
        result = []

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                elem = self.matrix[i][j]
                if Solution.is_symbol(elem):
                    # print(f'{elem}: {i, j}')
                    result.append(self.get_numbers(i - 1, j))
                    result.append(self.get_numbers(i + 1, j))
                    result.append(self.get_numbers(i, j + 1))
                    result.append(self.get_numbers(i, j - 1))
                    result.append(self.get_numbers(i - 1, j - 1))
                    result.append(self.get_numbers(i - 1, j + 1))
                    result.append(self.get_numbers(i + 1, j - 1))
                    result.append(self.get_numbers(i + 1, j + 1))
                    result = [i for i in result if i]

        print(f'Result: {sum(result)}')


if __name__ == "__main__":
    Solution().solve()
