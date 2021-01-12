from base import BaseSolution


class Node:
    @classmethod
    def parse(cls, data):
        node, _ = cls.parse_helper(data)
        return node

    @classmethod
    def parse_helper(cls, data):
        child_count, metadata_count, *rest = data
        children = []
        i = 0
        for _ in range(child_count):
            child, offset = cls.parse_helper(rest[i:])
            children.append(child)
            i += offset
        node = cls()
        node.metadata = rest[i : i + metadata_count]
        node.children = children
        return node, i + 2 + metadata_count

    def part1_value(self):
        return sum(self.metadata) + sum(child.part1_value() for child in self.children)

    def part2_value(self):
        if not self.children:
            return sum(self.metadata)
        return sum(
            self.children[i - 1].part2_value()
            for i in self.metadata
            if i - 1 in range(len(self.children))
        )


class Solution(BaseSolution):
    def load_data(self, input):
        data = [int(c) for c in input.split()]
        return Node.parse(data)

    def part1(self, root):
        return root.part1_value()

    def part2(self, root):
        return root.part2_value()

