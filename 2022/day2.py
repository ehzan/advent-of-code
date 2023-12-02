import file_handle


def puzzle3(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    games = [row.split(' ') for row in data.splitlines()]

    total_score = 0
    for [hand1, hand2] in games:
        hand1_value = ord(hand1) - ord('A') + 1
        hand2_value = ord(hand2) - ord('X') + 1
        match hand2_value - hand1_value:
            case -1 | 2:
                result = 0
            case 0:
                result = 1
            case 1 | -2:
                result = 2
        total_score += 3 * result + hand2_value

    return total_score


def puzzle4(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    games = [row.split(' ') for row in data.splitlines()]

    total_score = 0
    for [hand1, result] in games:
        hand1_value = ord(hand1) - ord('A') + 1
        result = ord(result) - ord('X')
        match result:
            case 0:  # lose
                hand2_value = (hand1_value + 1) % 3 + 1
            case 1:  # draw
                hand2_value = hand1_value
            case 2:  # win
                hand2_value = hand1_value % 3 + 1
        total_score += 3 * result + hand2_value

    return total_score


if __name__ == '__main__':
    print('Day #2, part one:', puzzle3('./input/day2.txt'))
    print('Day #2, part two:', puzzle4('./input/day2.txt'))
