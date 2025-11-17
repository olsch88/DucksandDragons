import time
from itertools import permutations
from collections import deque


def read_data(filename: str) -> list[tuple[int, str]]:
    with open(filename) as f:
        data = f.readlines()
    genes = []
    for line in data:
        genes.append((int(line.strip().split(":")[0]), line.strip().split(":")[1]))
    return genes


def is_child(child_candidate: str, parent1: str, parent2: str) -> bool:
    for genes in zip(child_candidate, parent1, parent2):
        if genes[0] not in genes[1:]:
            return False

    return True


def calc_similarity(gene1: tuple[int, str], gene2: tuple[int, str]):
    counter = 0
    for pair in zip(gene1[1], gene2[1]):
        if pair[0] == pair[1]:
            counter += 1
    return counter


def calc_degree_similarity(
    family: tuple[tuple[int, str], tuple[int, str], tuple[int, str]],
) -> int:
    matches_parent_1 = calc_similarity(family[0], family[1])
    matches_parent_2 = calc_similarity(family[0], family[2])
    return matches_parent_1 * matches_parent_2


def solve_part1(gene_sequences: list[tuple[int, str]]) -> int:
    perms = permutations(gene_sequences, 3)
    family = ((0, ""), (0, ""), (0, ""))
    for per in perms:
        if is_child(per[0][1], per[1][1], per[2][1]):
            family = per
            break
    return calc_degree_similarity(family)


def solve_part2(gene_sequences: list[tuple[int, str]]) -> int:
    perms = permutations(gene_sequences, 3)
    sum_similarities = 0
    for per in perms:
        if is_child(per[0][1], per[1][1], per[2][1]):
            sum_similarities += calc_degree_similarity(per)
    return sum_similarities // 2  # dividing by two, because we find every family twice


def get_family(related: dict[int, set[int]], start: int) -> set[int]:
    found = set()
    current = start
    queue = deque()
    found.add(start)
    queue.append(current)
    while len(queue) != 0:
        current = queue.popleft()
        for element in related[current]:
            if element not in found:
                found.add(element)
                queue.append(element)
    return found


def solve_part3(gene_sequences: list[tuple[int, str]]) -> int:
    perms = permutations(gene_sequences, 3)
    related: dict[int, set[int]] = dict()
    for i in range(1, len(gene_sequences) + 1):
        related[i] = set((i,))
    for per in perms:
        if is_child(per[0][1], per[1][1], per[2][1]):
            related[per[0][0]].add(per[1][0])
            related[per[0][0]].add(per[2][0])

            related[per[1][0]].add(per[0][0])
            related[per[1][0]].add(per[2][0])

            related[per[2][0]].add(per[0][0])
            related[per[2][0]].add(per[1][0])

    len_largest = 0
    largest = set()
    checked = set()
    for i in range(1, len(gene_sequences) + 1):
        if i in checked:
            continue
        checked.add(i)

        current_family = get_family(related, i)

        current_family_length = len(current_family)
        checked.update(current_family)
        if current_family_length > len_largest:
            len_largest = current_family_length
            largest = current_family

    return sum(largest)


def tests():
    assert solve_part1(read_data("q9_p1_example.txt")) == 414
    assert solve_part2(read_data("q9_p2_example.txt")) == 1245
    assert solve_part3(read_data("q9_p2_example.txt")) == 12
    assert solve_part3(read_data("q9_p3_example.txt")) == 36


if __name__ == "__main__":
    tests()
    start = time.perf_counter()
    print(f"Solution Part1: {solve_part1(read_data("q9_p1_input.txt"))}")
    print(f"Time Part 1: {time.perf_counter()-start:.3f} s")
    start = time.perf_counter()
    print(f"Solution Part2: {solve_part2(read_data("q9_p2_input.txt"))}")
    print(f"Time Part 2: {time.perf_counter()-start:.3f} s")
    start = time.perf_counter()
    print(f"Solution Part3: {solve_part3(read_data("q9_p3_input.txt"))}")
    print(f"Time Part 3: {time.perf_counter()-start:.3f} s")
