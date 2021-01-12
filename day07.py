from collections import defaultdict
from copy import deepcopy
from heapq import *

from base import BaseSolution


class Solution(BaseSolution):
    def load_data(self, input):
        deps = defaultdict(set)
        for line in input.splitlines():
            words = line.split()
            dep, step = words[1], words[7]
            if dep not in deps:
                deps[dep] = set()
            deps[step].add(dep)
        return deps

    def part1(self, deps):
        deps = deepcopy(deps)
        steps = []
        while deps:
            next_step = next(step for step in sorted(deps) if not deps[step])
            steps.append(next_step)
            deps.pop(next_step)
            for step in deps:
                if next_step in deps[step]:
                    deps[step].remove(next_step)
        return "".join(steps)

    def part2(self, deps):
        deps = deepcopy(deps)
        steps = []
        tasks = []
        workers = 5
        time = 0
        while deps:
            available_workers = workers - len(tasks)
            for _ in range(available_workers):
                try:
                    next_step = next(
                        step
                        for step in sorted(deps)
                        if not deps[step] and step not in self.get_active_steps(tasks)
                    )
                except StopIteration:
                    continue
                heappush(tasks, (self.get_cost(next_step), next_step))
            elapsed, next_step = heappop(tasks)
            time += elapsed
            tasks = [(cost - elapsed, step) for cost, step in tasks]
            steps.append(next_step)
            deps.pop(next_step)
            for step in deps:
                if next_step in deps[step]:
                    deps[step].remove(next_step)
        return time

    def get_cost(self, step):
        return 60 + ord(step) - ord("A") + 1

    def get_active_steps(self, tasks):
        return {step for _, step in tasks}


if __name__ == "__main__":
    from run import run

    run(["day07"])

