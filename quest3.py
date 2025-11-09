from collections import Counter
import time


def read_crates(filename: str) -> list[int]:
    with open(filename) as f:
        data = f.readline()
    crates = [int(i) for i in data.strip().split(",")]
    return crates


def solve_part1(crates: list[int]):
    stack = set(crates)
    return sum(stack)


def solve_part2(crates: list[int]):
    stack = set(crates)
    stack_list = list(stack)
    stack_list.sort()
    return sum(stack_list[:20])


def solve_part3(crates: list[int]):
    counts = Counter(crates)
    most = counts.most_common(1)
    return most[0][1]


def tests():
    assert solve_part1(read_crates("q3_p1_example.txt")) == 29
    assert solve_part2(read_crates("q3_p2_example.txt")) == 781
    assert solve_part3(read_crates("q3_p3_example.txt")) == 3


if __name__ == "__main__":
    tests()
    start = time.perf_counter()
    print(f"Solution Part1: {solve_part1(read_crates("q3_p1_input.txt"))}")
    print(f"Time Part 1: {time.perf_counter()-start:.3f} s")
    start = time.perf_counter()
    print(f"Solution Part2: {solve_part2(read_crates("q3_p2_input.txt"))}")
    print(f"Time Part 2: {time.perf_counter()-start:.3f} s")
    start = time.perf_counter()
    print(f"Solution Part3: {solve_part3(read_crates("q3_p3_input.txt"))}")
    print(f"Time Part 3: {time.perf_counter()-start:.3f} s")
