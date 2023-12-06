class Solution:
    def __init__(self, file_name='input'):
        with open(file_name, 'r') as f:
            self.data = f.read()
            lines = self.data.split('\n')
            self.times = [int(x) for x in lines[0].split()[1:]]
            self.records = [int(x) for x in lines[1].split()[1:]]

    def get_winning_races(self, idx: int) -> int:
        time = self.times[idx]
        distance = self.records[idx]

        res = 0
        for ms in range(1, time):
            rec = (time - ms) * ms
            if rec > distance:
                res += 1

        return res

    def solve(self):
        result = []
        for i in range(len(self.times)):
            result.append(self.get_winning_races(i))

        mul = 1
        for x in result:
            mul *= x
        print(f'Result: {mul}')


if __name__ == "__main__":
    Solution().solve()
