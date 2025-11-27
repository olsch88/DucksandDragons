from collections import deque
import time

DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def read_data(filename: str) -> list[str]:
    with open(filename) as f:
        data = f.readline()
    instructions = data.split(",")
    return instructions


def create_maze(
    instructions: list[str],
) -> tuple[set[tuple[int, int]], tuple[int, int]]:
    current_pos = (0, 0)
    wall: set[tuple[int, int]] = {current_pos}
    wall.add(current_pos)
    pos_in_directions = 0 if instructions[0][0] == "L" else 2
    for i in range(int(instructions[0][1:])):
        current_pos = (
            current_pos[0] + DIRECTIONS[pos_in_directions][0],
            current_pos[1] + DIRECTIONS[pos_in_directions][1],
        )
        wall.add(current_pos)
    for ins in instructions[1:]:
        if ins[0] == "L":
            pos_in_directions += 1
            pos_in_directions %= len(DIRECTIONS)
        else:
            pos_in_directions -= 1
            if pos_in_directions < 0:
                pos_in_directions += len(DIRECTIONS)
        for i in range(int(ins[1:])):
            current_pos = (
                current_pos[0] + DIRECTIONS[pos_in_directions][0],
                current_pos[1] + DIRECTIONS[pos_in_directions][1],
            )
            wall.add(current_pos)
    return wall, current_pos


def solve_part1(data: list[str]) -> int:
    maze, final_point = create_maze(data)
    print(final_point)
    maze.remove(final_point)
    start_pos = (0, 0)
    max_y = 0
    max_x = 0
    min_y = 0
    min_x = 0
    for element in maze:
        if element[0] > max_y:
            max_y = element[0]
        if element[1] > max_x:
            max_x = element[1]
        if element[0] < min_y:
            min_y = element[0]
        if element[1] < min_x:
            min_x = element[1]
    visited = set()
    length = 0
    queue = deque()
    queue.append((start_pos, length))
    while len(queue) != 0:
        current_pos, current_length = queue.popleft()
        # print(current_pos)
        if current_pos == final_point:
            return current_length
        for dire in DIRECTIONS:
            next_pos = (current_pos[0] + dire[0], current_pos[1] + dire[1])
            if next_pos[0] > max_y or next_pos[1] > max_x:
                continue
            if next_pos not in visited and next_pos not in maze:
                queue.append((next_pos, current_length + 1))
                visited.add(next_pos)
    return 0


if __name__ == "__main__":
    start = time.perf_counter()
    print(f"Solution Part1: {solve_part1(read_data("q15_p1_input.txt"))}")
    print(f"Time Part 1: {time.perf_counter()-start:.3f} s")
    start = time.perf_counter()
    print(f"Solution Part2: {solve_part1(read_data("q15_p2_input.txt"))}")
    print(f"Time Part 2: {time.perf_counter()-start:.3f} s")
    start = time.perf_counter()
    print(f"Solution Part3: {solve_part1(read_data("q15_p3_input.txt"))}")
    print(f"Time Part 3: {time.perf_counter()-start:.3f} s")
