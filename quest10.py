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


def get_sheep_grid(grid: list[str]) -> list[list[str]]:
    sheep_grid = [["S" if symbol == "S" else "." for symbol in line] for line in grid]
    return sheep_grid


def get_hide_grid(grid: list[str]) -> list[list[str]]:
    hide_grid = [["#" if symbol == "#" else "." for symbol in line] for line in grid]
    return hide_grid


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


def tests():
    assert solve_part1(read_data("Q10_p1_example.txt"), 3) == 27


if __name__ == "__main__":
    tests()
    print(solve_part1(read_data("Q10_p1_input.txt"), 4))
