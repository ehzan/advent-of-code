def main():
    for day in [15]:
        exec('import day{}'.format(day))
        print('Answer #{}: '.format(2 * day - 1), eval('day{}.puzzle{}()'.format(day, 2 * day - 1)), )
        print('Answer #{}: '.format(2 * day), eval('day{}.puzzle{}()'.format(day, 2 * day)), )


if __name__ == '__main__':
    main()
