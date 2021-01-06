from collections import defaultdict

from base import BaseSolution


class Solution(BaseSolution):
    def part1(self, lines):
        return sum(int(line) for line in lines)

    def part2(self, lines):
        frequency = 0
        counts = defaultdict(int)
        counts[frequency] = 1
        while True:
            for line in lines:
                frequency += int(line)
                counts[frequency] += 1
                if counts[frequency] > 1:
                    return frequency
