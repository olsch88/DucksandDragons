import time


def read_data(filename: str) -> list[int]:
    with open(filename) as f:
        data = f.readline()
    numbers = [int(n) for n in data.split(",")]
    return numbers


def intersect(line1: tuple[int, int], line2: tuple[int, int]) -> bool:
    """linien schneiden sich, wenn
    ein punkt kleiner ist als das maximum und größer als das minimum un der andere punkt größer ist als das maximum des anderen punktes
    """
    if max(line2) > max(line1) and min(line2) < max(line1) and min(line2) > min(line1):
        return True
    if max(line1) > max(line2) and min(line1) < max(line2) and min(line1) > min(line2):
        return True
    return False


def solve_part1(numbers: list[int], circle_length: int) -> int:
    length = len(numbers)
    crossings = 0
    for i, n in enumerate(numbers[:-1]):
        if abs(n - numbers[i + 1]) == circle_length // 2:
            crossings += 1
    return crossings


def solve_part2(numbers: list[int]) -> int:
    pairs = []
    for i, number in enumerate(numbers[:-1]):
        pairs.append((number, numbers[i + 1]))

    intersects = 0
    for i, pair in enumerate(pairs[1:]):
        for j in range(i):
            intersects += intersect(pair, pairs[j])

    return intersects


def tests():
    assert solve_part1(read_data("q8_p1_example.txt"), 8) == 4
    assert intersect((1, 5), (2, 5)) == False
    assert intersect((2, 5), (1, 5)) == False
    assert intersect((2, 6), (1, 5)) == True
    assert intersect((1, 5), (2, 6)) == True
    assert intersect((8, 6), (1, 5)) == False
    assert intersect((6, 8), (1, 5)) == False
    assert intersect((7, 3), (1, 5)) == True
    assert intersect((7, 3), (8, 6)) == True
    assert intersect((7, 3), (1, 4)) == True
    assert intersect((7, 8), (8, 6)) == False
    assert intersect((7, 5), (1, 5)) == False
    assert intersect((7, 5), (6, 2)) == True
    assert solve_part2(read_data("q8_p2_example.txt")) == 21


if __name__ == "__main__":
    tests()
    start = time.perf_counter()
    print(f"Solution Part1: {solve_part1(read_data("q8_p1_input.txt"),32)}")
    print(f"Time Part 1: {time.perf_counter()-start:.3f} s")
    start = time.perf_counter()
    print(f"Solution Part2: {solve_part2(read_data("q8_p2_input.txt"))}")
    print(f"Time Part 2: {time.perf_counter()-start:.3f} s")
    # start = time.perf_counter()
    # print(f"Solution Part3: {solve_part3(*read_input("q7_p3_input.txt"))}")
    # print(f"Time Part 3: {time.perf_counter()-start:.3f} s")
