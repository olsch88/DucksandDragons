import time


def read_data(filename: str) -> list[int]:
    with open(filename) as f:
        data = f.readlines()
    numbers = [int(line.strip()) for line in data]

    return numbers


def move_right(ducks: list[int], max_rounds=-1) -> int:
    moved = True
    rounds = 0
    while moved:
        if rounds == max_rounds:
            break
        rounds += 1
        moved = False
        for i in range(len(ducks) - 1):
            if ducks[i] > ducks[i + 1]:
                ducks[i] -= 1
                ducks[i + 1] += 1
                moved = True
    return rounds - 1


def move_left(ducks: list[int], max_rounds=-1) -> int:
    moved = True
    rounds = 0
    while moved:
        if rounds == max_rounds:
            break
        rounds += 1
        moved = False
        for i in range(len(ducks) - 1):
            if ducks[i + 1] > ducks[i]:
                ducks[i + 1] -= 1
                ducks[i] += 1
                moved = True
    return rounds - 1


def calc_checksum(ducks: list[int]) -> int:
    total = 0
    for i, duck in enumerate(ducks, start=1):
        total += i * duck
    return total

def move_left_v2(ducks: list[int], max_rounds=-1) -> int:
    min_pos=0
    max_pos=0
    moved=True
    rounds = 0
    while moved:
        moved = False
        min_pos=ducks.index(min(ducks))
        max_pos=ducks.index(max(ducks))
        if ducks[min_pos]==ducks[max_pos]:# all sorted
            break
        ducks[min_pos]+=1
        ducks[max_pos]-=1
        moved=True
        rounds +=1
    return rounds

def move_left_v3(ducks: list[int], max_rounds=-1) -> int:
    min_pos=0
    max_pos=0
    moved=True
    rounds = 0
    average=sum(ducks)//len(ducks)
    for i in range(len(ducks)):
        if ducks[i]<average:
            rounds+=average-ducks[i]
    return rounds
            

def tests():
    assert move_right([9, 1, 1, 4, 9, 6]) == 6
    assert calc_checksum([9, 1, 1, 4, 9, 6]) == 111
    assert solve_part1(read_data("q11_p1_example.txt")) == 109
    assert solve_part2(read_data("q11_p2_example1.txt")) == 11
    assert solve_part2(read_data("q11_p2_example2.txt")) == 1579


def solve_part1(ducks: list[int]) -> int:
    max_rounds = 10
    used_rounds = move_right(ducks, max_rounds)
    used_rounds = move_left(ducks, max_rounds - used_rounds)
    return calc_checksum(ducks)



def solve_part2(ducks: list[int]) -> int:
    # mini_duck= min(ducks)
    # ducks = [duck - mini_duck for duck in ducks]
    # print(max(ducks)-min(ducks))
    moves = move_right(ducks)
    moves += move_left_v3(ducks)
    return moves


def solve_part3(ducks: list[int]) -> int:
    return 0    # moves = 0
    # for i in range(len(ducks[:-1])):
    #     moves += ducks[i + 1] - ducks[i]
    # return moves


if __name__ == "__main__":
    tests()
    start = time.perf_counter()
    print(f"Solution Part1: {solve_part1(read_data("q11_p1_input.txt"))}")
    print(f"Time Part 1: {time.perf_counter()-start:.3f} s")
    start = time.perf_counter()
    print(f"Solution Part2: {solve_part2(read_data("q11_p2_input.txt"))}")
    print(f"Time Part 2: {time.perf_counter()-start:.3f} s")
    start = time.perf_counter()
    print(f"Solution Part3: {solve_part2(read_data("q11_p3_input.txt"))}")
    print(f"Time Part 3: {time.perf_counter()-start:.3f} s")
