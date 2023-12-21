import file_handle


def find_starting_position(garden: list[str]) -> tuple[int, int]:
    for y, row in enumerate(garden):
        if 'S' in row:
            return row.index('S'), y


def neighbors(position: tuple[int, int], garden: list[list[str]], infinite: bool = False
              ) -> set[tuple[int, int]]:
    (x, y) = position
    cols, rows = len(garden[0]), len(garden)
    adjacent_cells = {(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)}
    return {(x, y) for x, y in adjacent_cells
            if garden[y % rows][x % cols] != '#' and
            (infinite or 0 <= x < cols and 0 <= y < rows)}


def sequence(a: list[int], n: int) -> int:
    d1 = a[1] - a[0]
    d2 = a[2] - a[1]
    # dᵢ = dᵢ₋₁ + (d₂-d₁) = d₂ + (i-2)*(d₂-d₁)
    # aₙ = a₁ + Σᵢ₌₂܅ₙ dᵢ = a₁ + (n-1)*d₂ + (n-2)(n-1)/2 *(d₂-d₁)
    return a[1] + (n - 1) * d2 + (d2 - d1) * (n - 2) * (n - 1) // 2


def puzzle41(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    garden = data.splitlines()

    s = find_starting_position(garden)
    parity = (s[0] + s[1]) % 2

    visited = boundary = {s}
    for _ in range(64):
        next_boundary = {(nx, ny) for pos in boundary
                         for (nx, ny) in neighbors(pos, garden)
                         if (nx, ny) not in visited}
        visited.update(next_boundary)
        boundary = next_boundary

    reached = {(x, y) for (x, y) in visited if (x + y) % 2 == parity}
    return len(reached)


def puzzle42(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    garden = data.splitlines()

    s = find_starting_position(garden)
    parity = (s[0] + s[1]) % 2
    rows = len(garden)
    STEPS = 26501365

    visited = boundary = {s}
    a = []
    for i in range(1, STEPS):
        next_boundary = {(nx, ny) for pos in boundary
                         for (nx, ny) in neighbors(pos, garden, True)
                         if (nx, ny) not in visited}
        visited.update(next_boundary)
        boundary = next_boundary

        if i % rows == STEPS % rows:
            reached = {(x, y) for (x, y) in visited if (x + y + i) % 2 == parity}
            a.append(len(reached))
            if len(a) == 4:
                break

    assert a[3] == sequence(a, 3)
    return sequence(a, n=STEPS // rows)


if __name__ == '__main__':
    print('Day #21, part one:', puzzle41('./input/day21.txt'))
    print('Day #21, part two:', puzzle42('./input/day21.txt'))
