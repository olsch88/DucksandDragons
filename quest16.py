import time


def read_data(filename: str) -> list[int]:
    with open(filename) as f:
        data = f.readline()
    numbers = [int(n) for n in data.split(",")]
    return numbers


def generate_wall(numbers: list[int], length=90) -> list[int]:
    wall = [0] * length
    for n in numbers:
        for i in range(n - 1, length, n):
            wall[i] += 1
    return wall


def solve_part1(numbers: list[int]) -> int:
    length = 90
    total = 0
    for number in numbers:
        total += length // number
    return total


def solve_part2(wall: list[int]) -> int:
    spell = [1]
    for i, number in enumerate(wall, start=1):
        if generate_wall(spell, length=i) == wall[:i]:
            continue
        else:
            spell.append(i)
    total = 1
    for n in spell:
        total *= n

    return total


def tests():
    assert solve_part1(read_data("q16_p1_example.txt")) == 193
    assert solve_part2(read_data("q16_p2_example.txt")) == 270


if __name__ == "__main__":
    tests()
    # print(generate_wall(read_data("q16_p1_example.txt")))
    # print(solve_part2(read_data("q16_p2_example.txt")))
    start = time.perf_counter()
    print(f"Solution Part1: {solve_part1(read_data("q16_p1_input.txt"))}")
    print(f"Time Part 1: {time.perf_counter()-start:.3f} s")
    start = time.perf_counter()
    print(f"Solution Part2: {solve_part2(read_data("q16_p2_input.txt"))}")
    print(f"Time Part 2: {time.perf_counter()-start:.3f} s")
    # start = time.perf_counter()
    # print(f"Solution Part3: {solve_part1(read_data("q16_p3_input.txt"))}")
    # print(f"Time Part 3: {time.perf_counter()-start:.3f} s")
