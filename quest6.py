import time


def read_notes(filename: str) -> str:
    with open(filename) as f:
        data = f.readline()
    return data


def count_mentorings(notes: str, letter: str) -> int:
    mentor = letter.upper()
    novice = letter.lower()
    possible_pairs = 0
    for i, char in enumerate(notes):
        if char == mentor:
            possible_pairs += notes[i:].count(novice)
    return possible_pairs


def solve_part1(notes: str) -> int:
    return count_mentorings(notes, "a")


def solve_part2(notes: str) -> int:
    categories = set(notes.upper())
    total_pairs = 0
    for cat in categories:
        total_pairs += count_mentorings(notes, cat)
    return total_pairs


def solve_part3(notes: str) -> int:
    return 0


def tests():
    assert solve_part1(read_notes("q6_p1_example1.txt")) == 5
    assert solve_part2(read_notes("q6_p2_example.txt")) == 11


if __name__ == "__main__":
    tests()
    start = time.perf_counter()
    print(f"Solution Part1: {solve_part1(read_notes("q6_p1_input.txt"))}")
    print(f"Time Part 1: {time.perf_counter()-start:.3f} s")
    start = time.perf_counter()
    print(f"Solution Part2: {solve_part2(read_notes("q6_p2_input.txt"))}")
    print(f"Time Part 2: {time.perf_counter()-start:.3f} s")
    # start = time.perf_counter()
    # print(f"Solution Part3: {solve_part3(*read_data_part2("q5_p3_input.txt"))}")
    # print(f"Time Part 3: {time.perf_counter()-start:.3f} s")
