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


def find_pairs(notes:str, repeats: int, distance: int)->int:
    pairs=0
    length = len(notes)
    full_notes= notes*repeats
    for pos, char in enumerate(full_notes):
        #search for novice
        if char != char.lower():
            continue
        start =max(0,pos-distance )
        stop = min(pos+distance+1,len(full_notes))
        pairs+=full_notes[start:stop].count(char.upper())
    return pairs
        
            

def solve_part3(notes: str, rep=1, distance=10) -> int:
    number = find_pairs(notes, rep, distance)
    return number


def tests():
    assert solve_part1(read_notes("q6_p1_example1.txt")) == 5
    assert solve_part2(read_notes("q6_p2_example.txt")) == 11
    assert solve_part3(read_notes("q6_p3_example1.txt"))==34
    assert solve_part3(read_notes("q6_p3_example2.txt"), 2,10)==72
    assert solve_part3(read_notes("q6_p3_example2.txt"), 1000,1000)==3442321
if __name__ == "__main__":
    tests()
    start = time.perf_counter()
    print(f"Solution Part1: {solve_part1(read_notes("q6_p1_input.txt"))}")
    print(f"Time Part 1: {time.perf_counter()-start:.3f} s")
    start = time.perf_counter()
    print(f"Solution Part2: {solve_part2(read_notes("q6_p2_input.txt"))}")
    print(f"Time Part 2: {time.perf_counter()-start:.3f} s")
    start = time.perf_counter()
    print(f"Solution Part3: {solve_part3(read_notes("q6_p3_input.txt"), 1000, 1000)}")
    print(f"Time Part 3: {time.perf_counter()-start:.3f} s")
