import time
def read_data(filename: str)-> list[list[int]]:
    with open(filename) as f:
        data = f.readlines()
    grid =[[int(char)for char in line.strip()]for line in data]
    return grid

def tests():
    pass

def solve_part1():
    pass

def solve_part2():
    pass
def solve_part3():
    pass
if __name__ == "__main__":
    tests()
    start = time.perf_counter()
    print(f"Solution Part1: {solve_part1(read_data("q11_p1_input.txt"))}")
    print(f"Time Part 1: {time.perf_counter()-start:.3f} s")
    start = time.perf_counter()
    print(f"Solution Part2: {solve_part2(read_data("q11_p2_input.txt"))}")
    print(f"Time Part 2: {time.perf_counter()-start:.3f} s")
    start = time.perf_counter()
    print(f"Solution Part3: {solve_part2(read_data("q11_p3_input.txt"))}")
    print(f"Time Part 3: {time.perf_counter()-start:.3f} s")
