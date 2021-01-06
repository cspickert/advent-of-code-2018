import re
from collections import defaultdict
from datetime import datetime, timedelta

from base import BaseSolution


LINE_RE = re.compile(r"^\[(.*)\] (.*)$")

ONE_MINUTE = timedelta(minutes=1)


class Solution(BaseSolution):
    def load_data(self, input):
        entries = []
        for line in input.splitlines():
            match = LINE_RE.match(line)
            when = datetime.strptime(match.group(1), "%Y-%m-%d %H:%M")
            message = match.group(2)
            entries.append((when, message))
        asleep_minutes = defaultdict(lambda: defaultdict(int))
        guard_id, sleep_start = None, None
        for when, message in sorted(entries):
            if message.startswith("Guard"):
                guard_id = int(message.split()[1].lstrip("#"))
            elif message == "falls asleep":
                sleep_start = when
            elif message == "wakes up":
                for minute in self.get_minute_offset_range(sleep_start, when):
                    asleep_minutes[guard_id][minute] += 1
        return asleep_minutes

    def part1(self, data):
        total_asleep_minutes = {
            guard_id: sum(data[guard_id].values()) for guard_id in data
        }
        sleepiest_guard_id = max(
            total_asleep_minutes, key=lambda guard_id: total_asleep_minutes[guard_id],
        )
        most_asleep_minute = max(
            data[sleepiest_guard_id],
            key=lambda minute: data[sleepiest_guard_id][minute],
        )
        return sleepiest_guard_id * most_asleep_minute

    def part2(self, data):
        sleepiest_guard_id, most_asleep_minute, _ = max(
            [
                (guard_id, minute, data[guard_id][minute])
                for guard_id in data
                for minute in data[guard_id]
            ],
            key=lambda item: item[2],
        )
        return sleepiest_guard_id * most_asleep_minute

    def get_minute_offset_range(self, start, end):
        day_start = self.get_day_start(end)
        start_minute = self.get_delta_minutes(start - day_start)
        end_minute = self.get_delta_minutes(end - day_start)
        return range(start_minute, end_minute)

    def get_delta_minutes(self, delta):
        return int(delta.total_seconds() // ONE_MINUTE.total_seconds())

    def get_day_start(self, when):
        return datetime(when.year, when.month, when.day)
