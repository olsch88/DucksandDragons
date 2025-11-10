from dataclasses import dataclass
import time


def read_data(filename: str) -> tuple[int, list[int]]:
    with open(filename) as f:
        data = f.readline()
    sword_id = int(data.split(":")[0])
    bones = eval(data.split(":")[1])
    return sword_id, bones


def read_data_part2(filename: str) -> tuple[list[int], list[list[int]]]:
    with open(filename) as f:
        data = f.readlines()
    sword_ids = []
    bones = []
    for line in data:
        sword_ids.append(line.strip().split(":")[0])
        bones.append(eval(line.strip().split(":")[1]))
    return sword_ids, bones


@dataclass
class Node:
    value: int
    left: int = 0
    right: int = 0


def solve_part1(bones: list[int]) -> int:
    nodes: list[Node] = []
    nodes.append(Node(bones[0]))
    found = False
    for bone in bones[1:]:
        found = False
        for node in nodes:
            if bone > node.value and node.right == 0:
                node.right = bone
                found = True
                break
            elif bone < node.value and node.left == 0:
                node.left = bone
                found = True
                break
        if not found:
            nodes.append(Node(bone))
    spine = []
    for node in nodes:
        spine.append(str(node.value))
    return int("".join(spine))


def solve_part2(list_of_swords: list[list[int]]) -> int:
    max_quality = 0
    min_quality = 9999999999999999
    for sword in list_of_swords:
        quality = solve_part1(sword)
        if quality > max_quality:
            max_quality = quality
        elif quality < min_quality:
            min_quality = quality
    return max_quality - min_quality


if __name__ == "__main__":
    start = time.perf_counter()
    print(f"Solution Part1: {solve_part1(read_data("q5_p1_input.txt")[1])}")
    print(f"Time Part 1: {time.perf_counter()-start:.3f} s")
    start = time.perf_counter()
    print(f"Solution Part2: {solve_part2(read_data_part2("q5_p2_input.txt")[1])}")
    print(f"Time Part 2: {time.perf_counter()-start:.3f} s")
    # start = time.perf_counter()

    # print(f"Solution Part3: {solve_part3(read_data("q4_p3_input.txt"))}")
    # print(f"Time Part 3: {time.perf_counter()-start:.3f} s")
