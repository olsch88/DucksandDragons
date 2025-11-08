def read_input(filename: str) -> tuple[int, int]:
    with open(file=filename) as f:
        data = f.readline()
    output = data.strip().split("=")[1]
    output = output.strip("[]")
    output = (int(output.split(",")[0]), int(output.split(",")[1]))
    return output


def add(c1: tuple[int, int], c2: tuple[int, int]) -> tuple[int, int]:
    return (c1[0] + c2[0], c1[1] + c2[1])


def multiply(c1: tuple[int, int], c2: tuple[int, int]) -> tuple[int, int]:
    # [X1 * X2 - Y1 * Y2, X1 * Y2 + Y1 * X2]
    return (c1[0] * c2[0] - c1[1] * c2[1], c1[0] * c2[1] + c1[1] * c2[0])


def divide(c1: tuple[int, int], c2: tuple[int, int]) -> tuple[int, int]:
    return (int(c1[0] / c2[0]), int(c1[1] / c2[1]))


def solve_part1(A: tuple[int, int]) -> tuple[int, int]:
    result = (0, 0)

    for _ in range(3):
        result = multiply(result, result)
        result = divide(result, (10, 10))
        result = add(result, A)
    return result


def should_engrave(point: tuple[int, int]) -> bool:
    result = (0, 0)
    for _ in range(100):
        result = multiply(result, result)
        result = divide(result, (100_000, 100_000))
        result = add(result, point)
        if (
            result[0] > 1000000
            or result[0] < -1000000
            or result[1] > 1000000
            or result[1] < -1000000
        ):
            return False
    return True


def solve_part2(A: tuple[int, int]) -> int:
    engrave_count = 0
    for row in range(A[0], A[0] + 1001, 10):
        for col in range(A[1], A[1] + 1001, 10):
            engrave_count += should_engrave((row, col))
    return engrave_count


def solve_part3(A: tuple[int, int]) -> int:
    engrave_count = 0
    for row in range(A[0], A[0] + 1001, 1):
        for col in range(A[1], A[1] + 1001, 1):
            engrave_count += should_engrave((row, col))
    return engrave_count


def tests():
    assert add((1, 1), (2, 2)) == (3, 3)
    assert multiply((1, 1), (2, 2)) == (0, 4)
    assert multiply((-2, 5), (10, -1)) == (-15, 52)
    assert divide((10, 12), (2, 2)) == (5, 6)
    assert divide((-10, -12), (2, 2)) == (-5, -6)
    assert divide((-11, -12), (3, 5)) == (-3, -2)
    assert read_input("q2_p1_sample.txt") == (25, 9)
    assert should_engrave((35630, -64880)) == True
    assert should_engrave((35630, -64870)) == True
    assert should_engrave((36250, -64270)) == True
    assert should_engrave((35460, -64910)) == False
    assert should_engrave((35470, -64910)) == False
    assert should_engrave((35630, -64930)) == False
    assert solve_part2((35300, -64910)) == 4076
    assert solve_part3((35300, -64910)) == 406954


if __name__ == "__main__":
    tests()
    print(solve_part1(read_input("q2_p1_input.txt")))
    print(solve_part2(read_input("q2_p2_input.txt")))
    print(solve_part3(read_input("q2_p3_input.txt")))
