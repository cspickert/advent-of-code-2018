from collections import Counter, defaultdict

from base import BaseSolution


class Solution(BaseSolution):
    def part1(self, lines):
        count_counts = Counter(
            count for line in lines for count in set(Counter(line).values())
        )
        return count_counts[2] * count_counts[3]

    def part2(self, lines):
        for i in range(len(lines)):
            for j in range(i + 1, len(lines)):
                diff = [x for x, (a, b) in enumerate(zip(lines[i], lines[j])) if a != b]
                if len(diff) == 1:
                    return lines[i][: diff[0]] + lines[i][diff[0] + 1 :]
