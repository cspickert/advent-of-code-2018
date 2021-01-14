from base import BaseSolution


class Solution(BaseSolution):
    def load_data(self, input):
        serial_number = int(input)
        grid = [
            [self.get_power_level(serial_number, x, y) for x in range(1, 301)]
            for y in range(1, 301)
        ]
        return grid

    def part1(self, grid):
        _, result_x, result_y = max(
            (sum(c for row in grid[y : y + 3] for c in row[x : x + 3]), x, y)
            for y in range(len(grid) - 3)
            for x in range(len(grid[y]) - 3)
        )
        return f"{result_x + 1},{result_y + 1}"

    def part2(self, grid):
        # Note: I couldn't get this to run fast enough, so I rewrote it
        # in C (day11_part2.c). This is correct for size=3 though.
        _, result_x, result_y, size = max(
            (
                sum(c for row in grid[y : y + size] for c in row[x : x + size]),
                x,
                y,
                size,
            )
            for size in range(1, len(grid) + 1)
            for y in range(len(grid) - size)
            for x in range(len(grid[y]) - size)
        )
        return f"{result_x + 1},{result_y + 1},{size}"

    def get_power_level(self, serial_number, x, y):
        rack_id = x + 10
        power_level = rack_id * y + serial_number
        power_level *= rack_id
        power_level = int(str(power_level // 100)[-1])
        power_level -= 5
        return power_level

