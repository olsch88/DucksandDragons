import time


def read_gears(filename: str) -> list[int]:
    with open(filename) as f:
        data = f.readlines()
    numbers = [int(line.strip()) for line in data]
    return numbers


def read_gears_part3(filename: str) -> list[tuple[int, int]]:
    with open(filename) as f:
        data = f.readlines()
    gears = []
    gears.append((1, int(data[0])))
    for line in data[1:-1]:
        p1, p2 = line.strip().split("|")
        gears.append((int(p1), int(p2)))
    gears.append((int(data[-1]), 1))
    return gears


def tests():
    assert solve_part1(read_gears("q4_p1_example2.txt")) == 32400
    assert solve_part1(read_gears("q4_p1_example3.txt")) == 15888
    assert solve_part2(read_gears("q4_p1_example2.txt")) == 625000000000
    assert solve_part2(read_gears("q4_p1_example3.txt")) == 1274509803922
    assert solve_part3(read_gears_part3("q4_p3_example1.txt")) == 400
    assert solve_part3(read_gears_part3("q4_p3_example2.txt")) == 6818


def solve_part1(gears: list[int]) -> int:
    final_ratio = 1
    for i, gear in enumerate(gears[:-1]):
        final_ratio *= gear / gears[i + 1]
    return (final_ratio * 2025).__floor__()


def solve_part2(gears: list[int]) -> int:
    total_ratio = 1
    for i, gear in enumerate(gears[:-1]):
        total_ratio *= gear / gears[i + 1]
    return (10000000000000 / total_ratio).__ceil__()


def solve_part3(gears: list[tuple[int, int]]) -> int:
    total_ratio = 1
    for i, pair in enumerate(gears[:-1]):
        total_ratio *= pair[1] / gears[i + 1][0]
    return (total_ratio * 100).__floor__()


if __name__ == "__main__":
    tests()
    start = time.perf_counter()
    print(f"Solution Part1: {solve_part1(read_gears("q4_p1_input.txt"))}")
    print(f"Time Part 1: {time.perf_counter()-start:.3f} s")
    start = time.perf_counter()
    print(f"Solution Part2: {solve_part2(read_gears("q4_p2_input.txt"))}")
    print(f"Time Part 2: {time.perf_counter()-start:.3f} s")
    start = time.perf_counter()

    print(f"Solution Part3: {solve_part3(read_gears_part3("q4_p3_input.txt"))}")
    print(f"Time Part 3: {time.perf_counter()-start:.3f} s")
