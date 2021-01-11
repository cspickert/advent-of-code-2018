from collections import defaultdict

from base import BaseSolution


class Solution(BaseSolution):
    def load_data(self, input):
        return [tuple(map(int, line.split(", "))) for line in input.splitlines()]

    def part1(self, data):
        min_x = min(x for x, _ in data) - 1
        min_y = min(y for _, y in data) - 1
        max_x = max(x for x, _ in data) + 1
        max_y = max(y for _, y in data) + 1

        distances = defaultdict(list)

        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                for i, (data_x, data_y) in enumerate(data):
                    distances[x, y].append((i, abs(x - data_x) + abs(y - data_y)))

        min_distances = {}

        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                # Get the index in data with min distance for (x, y). If
                # there's no unique min distance, then don't set the
                # value in min_distances.
                min_dist_idx, min_dist = min(distances[x, y], key=lambda item: item[1])
                min_dist_count = sum(item[1] == min_dist for item in distances[x, y])
                if min_dist_count > 1:
                    continue
                min_distances[x, y] = min_dist_idx

        infinites = set()

        for x, y in min_distances:
            if x == min_x or y == min_y or x == max_x or y == max_y:
                infinites.add(min_distances[x, y])

        area_by_idx = defaultdict(int)

        for i, (x, y) in enumerate(data):
            if i in infinites:
                continue
            for other_x in range(min_x, max_x + 1):
                for other_y in range(min_y, max_y + 1):
                    if min_distances.get((other_x, other_y)) == i:
                        area_by_idx[i] += 1

        return max(area_by_idx.values())
