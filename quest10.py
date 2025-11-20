import time
from collections import deque


def read_data(filename: str) -> list[str]:
    with open(filename) as f:
        data = f.readlines()
    grid = [line.strip() for line in data]
    return grid


def find_start_pos(grid: list[str]) -> tuple[int, int]:
    for row, line in enumerate(grid):
        for col, symbol in enumerate(line):
            if symbol == "D":
                return (row, col)
    return (0, 0)

def get_sheep(grid: list[str]) -> set[tuple[int, int]]:
    sheep=set()
    for row, line in enumerate(grid):
        for col, symbol in enumerate(line):
            if symbol == "S":
                sheep.add((row, col))
    return sheep

def get_shelters(grid: list[str]) -> set[tuple[int, int]]:
    shelters=set()
    for row, line in enumerate(grid):
        for col, symbol in enumerate(line):
            if symbol == "#":
                shelters.add((row, col))
    return shelters

def solve_part1(grid: list[str], moves: int) -> int:
    start_pos = find_start_pos(grid)
    visited = set()
    queue = deque()
    steps = 0
    queue.append((start_pos, steps))
    n_sheep = 0
    while len(queue) != 0:
        current_pos, current_steps = queue.popleft()
        if current_pos in visited:
            continue
        visited.add(current_pos)
        try:
            if grid[current_pos[0]][current_pos[1]] == "S":
                n_sheep += 1
        except IndexError:  # out of bounds
            continue
        if current_steps < moves:
            queue.append(((current_pos[0] + 1, current_pos[1] + 2), current_steps + 1))
            queue.append(((current_pos[0] - 1, current_pos[1] + 2), current_steps + 1))
            queue.append(((current_pos[0] + 2, current_pos[1] + 1), current_steps + 1))
            queue.append(((current_pos[0] - 2, current_pos[1] + 1), current_steps + 1))
            queue.append(((current_pos[0] + 1, current_pos[1] - 2), current_steps + 1))
            queue.append(((current_pos[0] - 1, current_pos[1] - 2), current_steps + 1))
            queue.append(((current_pos[0] + 2, current_pos[1] - 1), current_steps + 1))
            queue.append(((current_pos[0] - 2, current_pos[1] - 1), current_steps + 1))
    return n_sheep

def move_sheep(sheep:set[tuple[int,int]], max_dist:int)-> set[tuple[int, int]]:
    new_sheep= set()
    for shoop in sheep:
        if shoop[0]==max_dist: # reached the bottom, removed in for next round
            continue
        new_sheep.add((shoop[0]+1, shoop[1]))
    
    return new_sheep

def move_dragon(dragon_positions:set[tuple[int,int]], max_col:int, max_row:int)-> set[tuple[int, int]]:
    new_dragon_positions=set()
    for pos in dragon_positions:
        new_dragon_positions.add((pos[0] + 1, pos[1] + 2))
        new_dragon_positions.add((pos[0] - 1, pos[1] + 2))
        new_dragon_positions.add((pos[0] + 2, pos[1] + 1))
        new_dragon_positions.add((pos[0] - 2, pos[1] + 1))
        new_dragon_positions.add((pos[0] + 1, pos[1] - 2))
        new_dragon_positions.add((pos[0] - 1, pos[1] - 2))
        new_dragon_positions.add((pos[0] + 2, pos[1] - 1))
        new_dragon_positions.add((pos[0] - 2, pos[1] - 1))
    trimmed_dragon_pos=set()
    for pos in new_dragon_positions: 
        if not max_row>=pos[0] >=0 and max_col>=pos[1]>=0:
            continue
        trimmed_dragon_pos.add(pos)
    
    return trimmed_dragon_pos

def eat_sheep(dragons:set[tuple[int,int]], sheep:set[tuple[int,int]], shelters:set[tuple[int,int]])->tuple[set[tuple[int,int]], int]:
    new_sheep=set()
    eaten=0
    for shoop in sheep:
        if shoop in dragons and shoop not in shelters:
            eaten+=1
            continue
        new_sheep.add(shoop)
    return new_sheep, eaten

def solve_part2(grid: list[str], moves: int) -> int:
    max_row=len(grid)
    max_col =len(grid[0])
    start_pos = find_start_pos(grid)
    dragons:set[tuple[int,int]]=set()
    dragons.add(start_pos)
    sheep =get_sheep(grid)
    shelters=get_shelters(grid)
    total_eaten=0
    for i in range(moves):
        dragons=move_dragon(dragons,max_col, max_row)
        sheep,eaten=eat_sheep(dragons, sheep, shelters)
        total_eaten+=eaten
        sheep=move_sheep(sheep, max_row)
        sheep,eaten=eat_sheep(dragons, sheep, shelters)
        total_eaten+=eaten
    return total_eaten


def tests():
    assert solve_part1(read_data("Q10_p1_example.txt"), 3) == 27
    assert solve_part2(read_data("Q10_p2_example.txt"), 3) == 27


if __name__ == "__main__":
    tests()
    start = time.perf_counter()
    print(f"Solution Part1: {solve_part1(read_data("q10_p1_input.txt"),4)}")
    print(f"Time Part 1: {time.perf_counter()-start:.3f} s")
    start = time.perf_counter()
    print(f"Solution Part2: {solve_part2(read_data("q10_p2_input.txt"),20)}")
    print(f"Time Part 2: {time.perf_counter()-start:.3f} s")
    # start = time.perf_counter()
    # print(f"Solution Part3: {solve_part3(read_data("q9_p3_input.txt"))}")
    # print(f"Time Part 3: {time.perf_counter()-start:.3f} s")
