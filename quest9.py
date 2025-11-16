import time


def read_data(filename: str) -> list[tuple[int, list[int]]]:
    with open(filename) as f:
        data = f.readline()
    genes=[]
    for line in data:
        genes.append((line.strip().split(":")))
    return numbers


def solve_part1(numbers: list[int], circle_length: int) -> int:
    return 0


def solve_part2(numbers: list[int]) -> int:
    return 0

def solve_part3(numbers:list[int], circle_length:int)->int:
    return 0

def tests():
    pass


if __name__ == "__main__":
    tests()
    start = time.perf_counter()
    print(f"Solution Part1: {solve_part1(read_data("q8_p1_input.txt"),32)}")
    print(f"Time Part 1: {time.perf_counter()-start:.3f} s")
    start = time.perf_counter()
    print(f"Solution Part2: {solve_part2(read_data("q8_p2_input.txt"))}")
    print(f"Time Part 2: {time.perf_counter()-start:.3f} s")
    start = time.perf_counter()
    print(f"Solution Part3: {solve_part3(read_data("q8_p3_input.txt"),256)}")
    print(f"Time Part 3: {time.perf_counter()-start:.3f} s")
