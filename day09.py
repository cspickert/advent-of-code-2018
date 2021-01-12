from collections import defaultdict, deque

from base import BaseSolution


class Solution(BaseSolution):
    def load_data(self, input):
        components = input.split()
        return tuple(map(int, (components[0], components[-2])))

    def part1(self, args):
        return self.play(*args)

    def part2(self, args):
        players, max_marble = args
        max_marble *= 100
        return self.play(players, max_marble)

    def play(self, players, max_marble):
        current_player = 1
        score = defaultdict(int)
        marbles = iter(range(1, max_marble + 1))
        circle = deque([0])
        while True:
            try:
                marble = next(marbles)
            except StopIteration:
                break
            if marble > 0 and marble % 23 == 0:
                score[current_player] += marble
                circle.rotate(7)
                score[current_player] += circle.popleft()
            else:
                circle.rotate(-2)
                circle.insert(0, marble)
            current_player += 1
            current_player %= players
        return max(score.values())
