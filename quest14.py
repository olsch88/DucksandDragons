import time
from collections import defaultdict
from pprint import pprint

def read_data(filename:str)->list[list[str]]:
    with open(filename) as f:
        data = f.readlines()
    grid=[[element for element in line.strip()] for line in data]
    return grid


def get_neighbors(size_y:int, size_x:int)->dict[tuple, list[tuple]]:
    neighbors=defaultdict(list)
    for row in range(size_y):
        for col in range(size_x):
            if col <size_x-1 and row <size_y-1:
                neighbors[(row, col)].append((row+1, col+1))
            if col >=1 and row >=1:
                neighbors[(row, col)].append((row-1, col-1))
            if col >=1 and row <size_y-1:
                neighbors[(row, col)].append((row+1, col-1))
            if col <size_x-1 and row >=1:
                neighbors[(row, col)].append((row-1, col+1))
    return neighbors

def process_turn(grid: list[list[str]])->list[list[str]]:
    neighbors = get_neighbors(len(grid), len(grid[0]))
    new_grid=[[""for _ in range(len(grid[0]))] for i in range(len(grid))]
    for y, row in enumerate(grid):
        for x, element in enumerate(row):
            if element =="#":
                diag_count=0
                for y_n, x_n in neighbors[(y,x)]:
                    if grid[y_n][x_n]=="#":
                        diag_count+=1
                if diag_count%2==1:
                    new_grid[y][x]="#"
                else:
                    new_grid[y][x]="."
            if element ==".":
                diag_count=0
                for y_n, x_n in neighbors[(y,x)]:
                    if grid[y_n][x_n]=="#":
                        diag_count+=1
                if diag_count%2==0:
                    new_grid[y][x]="#"
                else:
                    new_grid[y][x]="."
    return new_grid      
                    
def count_active(grid: list[list[str]])->int:
    count=0
    for row in grid:
        count+= row.count("#")
    return count

def solve_part1(grid:list[list[str]])-> int:
    total_count=0
    for _ in range(10):
        grid= process_turn(grid)
        total_count+=count_active(grid)
    return total_count

def solve_part2(grid:list[list[str]])-> int:
    total_count=0
    for _ in range(2025):
        grid= process_turn(grid)
        total_count+=count_active(grid)
    return total_count
        
    
#     dials=construct_dial(dials)
#     return dials[(2025%len(dials))]

# def solve_part2(numbers:list[str])-> int:
#     dials =construct_dial_part2(numbers)
#     return dials[(20252025%len(dials))]

# def solve_part3(numbers:list[str])-> int:
#     dials =construct_dial_part2(numbers)
#     return dials[(202520252025%len(dials))]

def tests():
    pass
    assert solve_part1(read_data("q14_p1_example.txt"))==200
    # assert solve_part2(read_data_part2("q13_p2_example.txt"))==30 
    # # assert solve_part3(read_data("q12_p3_example1.txt"))==14

if __name__ == "__main__":
    tests()
    start = time.perf_counter()
    print(f"Solution Part1: {solve_part1(read_data("q14_p1_input.txt"))}")
    print(f"Time Part 1: {time.perf_counter()-start:.3f} s")
    start = time.perf_counter()
    print(f"Solution Part2: {solve_part2(read_data("q14_p2_input.txt"))}")
    print(f"Time Part 2: {time.perf_counter()-start:.3f} s")
    # start = time.perf_counter()
    # print(f"Solution Part3: {solve_part3(read_data_part2("q13_p3_input.txt"))}")
    # print(f"Time Part 3: {time.perf_counter()-start:.3f} s")