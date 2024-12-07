import file_handle


# import itertools
# def is_possible(target: int, operands: list[int], use_concat_operator: bool = False) -> bool:
#     operator_types = ('+', '*', '||') if use_concat_operator else ('+', '*')
#
#     for operators in itertools.product(operator_types, repeat=len(operands) - 1, ):
#         r = operands[0]
#         for operand, operator in zip(operands[1:], operators):
#             match operator:
#                 case '+':
#                     r += operand
#                 case '*':
#                     r *= operand
#                 case '||':
#                     r = int(str(r) + str(operand))
#         if r == target:
#             return True
#
#     return False


def is_possible(target: int, operands: list[int], n: int, use_concat_operator: bool = False) -> bool:
    if n == 1:
        return target == operands[0]

    operand = operands[n - 1]
    # + operator
    feasible_targets = [target - operand]
    # * operator
    if target % operand == 0:
        feasible_targets.append(target // operand)
    # || operator
    k = len(str(operand))
    former, latter = str(target)[:-k], str(target)[-k:]
    if use_concat_operator and len(str(target)) > k and latter == str(operand):
        feasible_targets.append(int(former))

    return any(is_possible(new_target, operands, n - 1, use_concat_operator)
               for new_target in feasible_targets)


def puzzle13(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    equations = [row.split(': ') for row in data.splitlines()]
    equations = [(int(result), list(map(int, operands.split())),) for result, operands in equations]

    return sum(result for result, operands in equations
               if is_possible(result, operands, len(operands), ))


def puzzle14(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    equations = [row.split(': ') for row in data.splitlines()]
    equations = [(int(result), list(map(int, operands.split())),) for result, operands in equations]

    return sum(result for result, operands in equations
               if is_possible(result, operands, len(operands), True))


if __name__ == '__main__':
    print('Day #7, part one:', puzzle13('./input/day7.txt'))
    print('Day #7, part two:', puzzle14('./input/day7.txt'))
