from base import BaseSolution


class Solution(BaseSolution):
    def load_data(self, input_str):
        initial_state_str, rules_str = input_str.split("\n\n")
        initial_state = initial_state_str.split(": ")[1]
        rules = [line.split(" => ") for line in rules_str.splitlines()]
        return initial_state, rules

    def part1(self, data):
        initial_state, rules = data
        state = initial_state

        for _ in range(20):
            # Note: padding with an extra "." on the right is
            # necessary to ensure one of the rules matches on the
            # initial input.
            # Source: https://www.reddit.com/r/adventofcode/comments/a83dw4/2018_day_12_part_1_solution_fails_on_input/
            state = f"..{state}..."
            next_state = ""

            for i in range(2, len(state) - 2):
                for condition, result in rules:
                    if state[i - 2 : i + 3] == condition:
                        next_state += result
                        break
                else:
                    # Only needed for the example input.
                    next_state += "."

            state = f"..{next_state}.."

        return sum(i - 40 for i in range(len(state)) if state[i] == "#")

    def part2(self, data):
        pass
