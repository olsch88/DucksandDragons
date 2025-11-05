def read_names_and_instructions(filename: str) -> tuple[list, list]:
    with open(filename) as f:
        lines = f.readlines()
    names = lines[0].strip().split(",")
    instructions = lines[-1].strip().split(",")
    return names, instructions


def solve_part1(names: list[str], instructions: list[str]) -> str:
    position = 0
    length = len(names)
    for instr in instructions:
        direction = instr[0]
        step = int(instr[1])
        if direction == "R":
            position = min(length-1, position + step)
        else:
            position = max(0, position - step)

    return names[position]

def solve_part2(names: list[str], instructions: list[str]) -> str:
    position= 0
    length = len(names)
    step_total =0
    for instr in instructions:
        direction = instr[0]
        step = int(instr[1:])
        if direction == "R":
            step_total+=step
        else:
            step_total-=step
    print(step_total)
    return names[position+step_total]

def tests():
    assert solve_part1(*read_names_and_instructions("q1_p1_example.txt"))=="Fyrryn"
    assert solve_part2(*read_names_and_instructions("q1_p2_example.txt"))=="Elarzris"
    
if __name__ == "__main__":
    tests()
    
    print(solve_part1(*read_names_and_instructions("q1_p1_input.txt")))
    print(solve_part2(*read_names_and_instructions("q1_p2_input.txt")))