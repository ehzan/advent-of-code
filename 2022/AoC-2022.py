# if __name__ == '__main__':
for day in range(1, 15):
    exec('import day{}'.format(day))
    print()
    print('Day #{}, Part One:'.format(day), eval('day{}.puzzle{}()'.format(day, 2 * day - 1)), )
    print('Day #{}, Part Two:'.format(day), eval('day{}.puzzle{}()'.format(day, 2 * day)), )
