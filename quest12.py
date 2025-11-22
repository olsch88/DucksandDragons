import time
from collections import deque

def read_data(filename: str)-> list[list[int]]:
    with open(filename) as f:
        data = f.readlines()
    grid =[[int(char)for char in line.strip()]for line in data]
    return grid

def get_neighbors(pos:tuple[int, int], max_x:int, max_y:int)-> list[tuple[int, int]]:
    neighbors=[]
    if pos[0]>0:
        neighbors.append((pos[0]-1, pos[1]))
    if pos[0]<max_y-1:
        neighbors.append((pos[0]+1, pos[1]))
    if pos[1]>0:
        neighbors.append((pos[0], pos[1]-1))
    if pos[1]<max_x-1:
        neighbors.append((pos[0], pos[1]+1))
        
    return neighbors

def destroy_barrels(grid:list[list[int]], start_pos:tuple[int, int])->int:
    max_x=len(grid[0])
    max_y=len(grid)
    start_pos=start_pos
    queue= deque()
    queue.append(start_pos)
    visited=set()
    while len(queue)!=0:
        current_pos =queue.popleft()
        visited.add(current_pos)
        for pos in get_neighbors(current_pos, max_x, max_y):
            if pos in visited:
                continue
            if grid[pos[0]][pos[1]]<=grid[current_pos[0]][current_pos[1]]:
                queue.append(pos)
    return len(visited)

def solve_part1(grid:list[list[int]])->int:
    return destroy_barrels(grid, (0,0))

def solve_part2(grid:list[list[int]])->int:
    max_x=len(grid[0])
    max_y=len(grid)
    start_pos=(0,0)
    lower_corner=(max_y-1, max_x-1)
    queue= deque()
    queue.append(start_pos)
    queue.append(lower_corner)
    visited=set()
    while len(queue)!=0:
        current_pos =queue.popleft()
        visited.add(current_pos)
        for pos in get_neighbors(current_pos, max_x, max_y):
            if pos in visited or pos in queue:
                continue
            if grid[pos[0]][pos[1]]<=grid[current_pos[0]][current_pos[1]]:
                queue.append(pos)
    return len(visited)
    

def solve_part3(grid:list[list[int]])->int:
    counts=[]
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            print(y,x)
            print(destroy_barrels(grid, (y,x)))
            counts.append(destroy_barrels(grid, (y,x)))
            
    counts.sort(reverse=True)
    return sum(counts[:3])
            

def tests():
    assert solve_part1(read_data("q12_p1_example.txt"))==16
    assert solve_part2(read_data("q12_p2_example.txt"))==58
    assert solve_part3(read_data("q12_p3_example1.txt"))==14

if __name__ == "__main__":
    tests()
    start = time.perf_counter()
    print(f"Solution Part1: {solve_part1(read_data("q12_p1_input.txt"))}")
    print(f"Time Part 1: {time.perf_counter()-start:.3f} s")
    start = time.perf_counter()
    print(f"Solution Part2: {solve_part2(read_data("q12_p2_input.txt"))}")
    print(f"Time Part 2: {time.perf_counter()-start:.3f} s")
    # start = time.perf_counter()
    # print(f"Solution Part3: {solve_part2(read_data("q11_p3_input.txt"))}")
    # print(f"Time Part 3: {time.perf_counter()-start:.3f} s")
