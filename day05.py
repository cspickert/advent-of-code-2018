from base import BaseSolution


class Solution(BaseSolution):
    def load_data(self, input):
        return [c for c in input]

    def part1(self, data):
        return self.react(data)

    def part2(self, data):
        return min(
            self.react([c for c in data if c not in unit])
            for unit in self.enumerate_units(data)
        )

    def react(self, data):
        data = data[:]
        while True:
            updated = False
            i = 1
            while i < len(data):
                if data[i] != data[i - 1] and data[i].lower() == data[i - 1].lower():
                    data[i - 1 : i + 1] = []
                    i -= 2
                    updated = True
                i += 1
            if not updated:
                break
        return len(data)

    def enumerate_units(self, data):
        unique_chars = set(data)
        for char in unique_chars:
            if char == char.lower():
                yield (char, char.upper())
