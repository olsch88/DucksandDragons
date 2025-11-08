def read_crates(filename: str)-> list[int]:
    with open(filename) as f:
        data=f.readline()
    crates = [int(i) for i in data.strip().split(",")]
    return crates


def solve_part1(crates:list[int]):
    stack = set(crates)
    return sum(stack)

def solve_part2(crates:list[int]):
    stack = set(crates)
    stack_list= list(stack)
    stack_list.sort()
    return sum(stack_list[:20])

def tests():
    assert solve_part1(read_crates("q3_p1_example.txt"))==29
    assert solve_part2(read_crates("q3_p2_example.txt"))==781


if __name__=="__main__":
    print(read_crates("q3_p1_example.txt"))
    print(solve_part1(read_crates("q3_p1_input.txt")))
    print(solve_part2(read_crates("q3_p2_input.txt")))