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

    def number(self):
        string_number = "".join([str(self.left), str(self.value), str(self.right)])
        if self.left == 0:
            string_number = string_number.lstrip("0")
        if self.right == 0:
            string_number = string_number.rstrip("0")
        return int(string_number)


@dataclass
class Sword:
    id: int
    bones: list[Node]

    def calc_quality(self):
        spine = []
        for node in self.bones:
            spine.append(str(node.value))
        return int("".join(spine))


def better_sword(sword1: Sword, sword2: Sword):
    """returns true, if sword 1 is better, false otherwise"""
    if sword1.calc_quality() > sword2.calc_quality():
        return True
    elif sword1.calc_quality() < sword2.calc_quality():
        return False

    for levels in zip(sword1.bones, sword2.bones):
        if levels[0].number() > levels[1].number():
            return True
        elif levels[0].number() < levels[1].number():
            return False
    if sword1.id > sword2.id:
        return True
    return False


def create_bones(instructions: list[int]) -> list[Node]:
    nodes: list[Node] = []
    nodes.append(Node(instructions[0]))
    found = False
    for bone in instructions[1:]:
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
    return nodes


def sort_swords(sword_list: list[Sword]) -> list[Sword]:
    changed = True
    while changed:
        changed = False
        for pos in range(len(sword_list) - 1):
            if better_sword(sword_list[pos + 1], sword_list[pos]):
                sword_list[pos + 1], sword_list[pos] = (
                    sword_list[pos],
                    sword_list[pos + 1],
                )
                changed = True
    return sword_list


def calc_checksum(sword_list: list[Sword]) -> int:
    checksum = 0
    for i, Sword in enumerate(sword_list, start=1):
        checksum += i * Sword.id
    return checksum


def solve_part1(bones: list[int]) -> int:
    nodes = create_bones(bones)
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


def solve_part3(list_of_ids, list_of_sword_instructions: list[list[int]]) -> int:
    list_of_swords: list[Sword] = []
    for i, sword in enumerate(list_of_sword_instructions, start=1):
        list_of_swords.append(Sword(i, create_bones(sword)))
    sorted_swords = sort_swords(list_of_swords)

    return calc_checksum(sorted_swords)


if __name__ == "__main__":
    start = time.perf_counter()
    print(f"Solution Part1: {solve_part1(read_data("q5_p1_input.txt")[1])}")
    print(f"Time Part 1: {time.perf_counter()-start:.3f} s")
    start = time.perf_counter()
    print(f"Solution Part2: {solve_part2(read_data_part2("q5_p2_input.txt")[1])}")
    print(f"Time Part 2: {time.perf_counter()-start:.3f} s")
    start = time.perf_counter()
    print(f"Solution Part3: {solve_part3(*read_data_part2("q5_p3_input.txt"))}")
    print(f"Time Part 3: {time.perf_counter()-start:.3f} s")
