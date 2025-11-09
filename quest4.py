import time
def read_gears(filename: str)-> list[int]:
    with open(filename ) as f:
        data= f.readlines()
    numbers = [int(line.strip())for line in data]
    return numbers

def gcd(a:int, b:int)->int:
    return a if b == 0 else gcd(b, a % b)

def lcm(a:int, b:int)->int:
    return (a // gcd(a, b)) * b

def tests():
    pass

def lcm_multiple(numbers:list[int])->int:
    final=0
    for index, number in enumerate(numbers[:-1]):
        final = lcm(number, numbers[index+1])
    return final

def solve_part1(gears: list[int])->float:
    final_ratio=1
    for i, gear in enumerate(gears[:-1]):
        final_ratio*=gear/gears[i+1]
    return final_ratio *2025
    
    
    
if __name__ == '__main__':
    tests()
    print(lcm_multiple([128,64,32,16,8])*2025)
    print(lcm_multiple([102,75,50,35,13]))
    print(lcm(102, 75)/102)
    print(solve_part1([102,75,50,35,13]))
    print(solve_part1(read_gears("q4_p1_input.txt")))
    # start=time.perf_counter()    
    # print(f"Solution Part1: {solve_part1(read_crates("q3_p1_input.txt"))}")
    # print(f"Time Part 1: {time.perf_counter()-start:.3f} s")
    # start=time.perf_counter()
    # print(f"Solution Part2: {solve_part2(read_crates("q3_p2_input.txt"))}")
    # print(f"Time Part 2: {time.perf_counter()-start:.3f} s")
    # start=time.perf_counter()
    # print(f"Solution Part3: {solve_part3(read_crates("q3_p3_input.txt"))}")
    # print(f"Time Part 3: {time.perf_counter()-start:.3f} s")