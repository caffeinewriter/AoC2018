import os
from pathlib import Path
from datetime import datetime


def create_guard_buckets():
    active_guard = 0
    is_asleep = False
    sleep_time = 0
    guard_buckets = {}
    with open(Path(os.path.dirname(
            os.path.realpath(__file__))) / 'day4.txt') as f:
        schedules = sorted(f.read().splitlines())
        for schedule in schedules:
            schedule = schedule.split(' ', 2)
            schedule = [' '.join(schedule[:2]), ' '.join(schedule[2:])]
            time = datetime.strptime(schedule[0], '[%Y-%m-%d %H:%M]')
            if schedule[1][:5] == 'Guard':
                if is_asleep:
                    is_asleep = False
                    for i in range(sleep_time, time.minute):
                        guard_buckets[active_guard][i] += 1
                active_guard = schedule[1][6:].split(' ')[0][1:]
                if active_guard not in guard_buckets:
                    guard_buckets[active_guard] = [0 for x in range(60)]
            elif schedule[1][:5] == 'falls':
                is_asleep = True
                sleep_time = time.minute
            elif schedule[1][:5] == 'wakes':
                is_asleep = False
                for i in range(sleep_time, time.minute):
                    guard_buckets[active_guard][i] += 1
    return guard_buckets


def part_1():
    guard_buckets = create_guard_buckets()
    guard_buckets = sorted(guard_buckets.items(),
                           key=lambda x: sum(x[1]), reverse=True)
    return int(guard_buckets[0][0]) * guard_buckets[0][1].index(
        max(guard_buckets[0][1]))


def part_2():
    guard_buckets = create_guard_buckets()
    guard_buckets = sorted(guard_buckets.items(),
                           key=lambda x: max(x[1]), reverse=True)
    return int(guard_buckets[0][0]) * guard_buckets[0][1].index(
        max(guard_buckets[0][1]))


def print_solutions_for_day():
    print("Advent of Code 2018 Day 4:")
    print("Part 1 - " + str(part_1()))
    print("Part 2 - " + str(part_2()))


if __name__ == '__main__':
    print_solutions_for_day()
