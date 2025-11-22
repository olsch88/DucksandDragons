import time

def read_data(filename: str)-> list[int]:
    with open(filename) as f:
        data = f.readlines()
    dials =[int(line.strip()) for line in data]
    return dials

def construct_dial(numbers: list[int])-> list[int]:
    dials=[0]*(len(numbers)+1)
    dials[0]=1
    for i, num in enumerate(numbers):
        if i%2==0:
            dials[i//2+1]=num
        else: 
            dials[-i//2]=num
    return dials

def solve_part1(dials:list[int])-> int:
    dials=construct_dial(dials)
    return dials[(2025%len(dials))]

def tests():
    assert solve_part1(read_data("q13_p1_example.txt"))==67
    # assert solve_part2(read_data("q12_p2_example.txt"))==58
    # assert solve_part3(read_data("q12_p3_example1.txt"))==14

if __name__ == "__main__":
    tests()
    start = time.perf_counter()
    print(construct_dial(read_data("q13_p1_example.txt")))
    print(f"Solution Part1: {solve_part1(read_data("q13_p1_input.txt"))}")
    print(f"Time Part 1: {time.perf_counter()-start:.3f} s")
    # start = time.perf_counter()
    # print(f"Solution Part2: {solve_part2(read_data("q12_p2_input.txt"))}")
    # print(f"Time Part 2: {time.perf_counter()-start:.3f} s")
    # start = time.perf_counter()
    # print(f"Solution Part3: {solve_part2(read_data("q11_p3_input.txt"))}")
    # print(f"Time Part 3: {time.perf_counter()-start:.3f} s")
