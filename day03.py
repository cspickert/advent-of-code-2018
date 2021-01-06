import re
from collections import Counter, defaultdict

from base import BaseSolution


LINE_RE = re.compile(r"^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$")


class Solution(BaseSolution):
    def load_data(self, input):
        return [
            tuple(int(i) for i in LINE_RE.match(line).groups())
            for line in input.splitlines()
        ]

    def part1(self, data):
        counts = Counter(
            coords for _, *area in data for coords in self.get_all_coords(*area)
        )
        return sum(count > 1 for count in counts.values())

    def part2(self, entries):
        claims = defaultdict(set)
        for claim_id, *area in entries:
            for coords in self.get_all_coords(*area):
                claims[coords].add(claim_id)
        for claim_id, *area in entries:
            if all(
                claims[coords] == {claim_id} for coords in self.get_all_coords(*area)
            ):
                return claim_id

    def get_all_coords(self, start_x, start_y, w, h):
        return (
            (x, y)
            for x in range(start_x, start_x + w)
            for y in range(start_y, start_y + h)
        )
