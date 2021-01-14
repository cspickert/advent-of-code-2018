import re

from base import BaseSolution


LINE_RE = re.compile(r"^position=< *(-?\d+), *(-?\d+)> velocity=< *(-?\d+), *(-?\d+)>$")


class Solution(BaseSolution):
    def load_data(self, input):
        data = []
        for line in input.splitlines():
            match = LINE_RE.match(line)
            x, y, dx, dy = map(int, match.groups())
            data.append(((x, y), (dx, dy)))
        return data

    def part1(self, data):
        min_area, min_area_time = min(
            (self.get_area(data, time), time) for time in range(20000)
        )
        all_coords = self.get_all_coords(data, min_area_time)
        (min_x, min_y), (max_x, max_y) = self.get_bounds(all_coords)
        return self.get_message(all_coords, min_x, min_y, max_x, max_y)

    def part2(self, data):
        _, min_area_time = min(
            (self.get_area(data, time), time) for time in range(20000)
        )
        return min_area_time

    def get_area(self, data, time):
        all_coords = self.get_all_coords(data, time)
        (min_x, min_y), (max_x, max_y) = self.get_bounds(all_coords)
        return (max_x - min_x) * (max_y - min_y)

    def get_message(self, all_coords, min_x, min_y, max_x, max_y):
        grid = [[" " for x in range(min_x, max_x + 1)] for y in range(min_y, max_y + 1)]
        for x, y in all_coords:
            grid[y - min_y][x - min_x] = "#"
        return "\n".join("".join(row) for row in grid)

    def get_all_coords(self, data, time=0):
        return [(x + dx * time, y + dy * time) for (x, y), (dx, dy) in data]

    def get_bounds(self, all_coords):
        min_x = min(x for x, _ in all_coords)
        min_y = min(y for _, y in all_coords)
        max_x = max(x for x, _ in all_coords)
        max_y = max(y for _, y in all_coords)
        return (min_x, min_y), (max_x, max_y)
