import time
from collections import deque


def read_input(filename) -> tuple[list[str], dict]:
    with open(filename) as f:
        data = f.readlines()
    names = data[0].strip().split(",")

    rules = dict()
    for line in data[2:]:
        key, values = line.strip().split(">")
        key = key.strip()
        rules[key] = values.strip().split(",")

    return names, rules


def check_name(name: str, rules: dict) -> bool:
    for i, char in enumerate(name[:-1]):
        if name[i + 1] not in rules[char]:
            return False
    return True


def solve_part1(names: list[str], rules: dict) -> str:
    for name in names:
        if check_name(name, rules):
            return name
    return ""


def solve_part2(names: list[str], rules: dict) -> int:
    name_sum = 0
    for i, name in enumerate(names, start=1):
        if check_name(name, rules):
            name_sum += i
    return name_sum


def find_combinations(
    name: str, rules: dict, min_length: int = 7, max_length: int = 11
) -> set[str]:
    names_found = set()
    current_names = deque()
    current_names.append(name)
    while len(current_names) != 0:
        check_name = current_names.popleft()
        if len(check_name) >= min_length:
            names_found.add(check_name)
        if len(check_name) == max_length:
            continue
        if check_name[-1] in rules:
            for letter in rules[check_name[-1]]:

                current_names.append(check_name + letter)

    return names_found


def solve_part3(names: list[str], rules: dict) -> int:
    total_names_set = set()
    for name in names:
        if not check_name(name, rules):
            continue
        total_names_set.update(find_combinations(name, rules))
    return len(total_names_set)


def tests():
    assert solve_part1(*read_input("q7_p1_example.txt")) == "Oroneth"
    assert solve_part2(*read_input("q7_p2_example.txt")) == 23
    assert solve_part3(*read_input("q7_p3_example1.txt")) == 25


if __name__ == "__main__":
    tests()
    start = time.perf_counter()
    print(f"Solution Part1: {solve_part1(*read_input("q7_p1_input.txt"))}")
    print(f"Time Part 1: {time.perf_counter()-start:.3f} s")
    start = time.perf_counter()
    print(f"Solution Part2: {solve_part2(*read_input("q7_p2_input.txt"))}")
    print(f"Time Part 2: {time.perf_counter()-start:.3f} s")
    start = time.perf_counter()
    print(f"Solution Part3: {solve_part3(*read_input("q7_p3_input.txt"))}")
    print(f"Time Part 3: {time.perf_counter()-start:.3f} s")
