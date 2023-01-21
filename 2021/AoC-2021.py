def main():
    for day in [17]:
        exec(f'import day{day}')
        print(f'Day #{day}, Part One:', eval(f'day{day}.puzzle{2 * day - 1}("input.txt")'), )
        #
        # print(f'Day #{day}, Part One:', eval(f'day{day}.puzzle{2 * day - 1}("day{day}.txt")'), )
        # print(f'Day #{day}, Part Two:', eval(f'day{day}.puzzle{2 * day}("day{day}.txt")'), )


if __name__ == '__main__':
    main()
