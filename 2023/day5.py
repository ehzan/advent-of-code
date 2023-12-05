import file_handle


def parse_input(data: str) -> tuple[list[int], list[set]]:
    sections = data.split('\n\n')
    seeds = list(map(int, sections[0].split()[1:]))
    mappings = [{tuple(map(int, mapping_str.split()))
                 for mapping_str in mapping_section.splitlines()[1:]}
                for mapping_section in sections[1:]]

    return seeds, mappings


def convert(sources: set[int], mapping: set[tuple]) -> set[tuple]:
    destinations = set()
    for source in sources:
        for (d, s, r) in mapping:
            if s <= source < s + r:
                destinations.add(source + d - s)
                break
        else:
            destinations.add(source)

    return destinations


def convert_ranges(sources: set[tuple], mappings: [tuple]) -> set[tuple]:
    destinations = set()
    while sources:
        (start, end) = sources.pop()
        for (d, s, r) in mappings:
            offset = d - s
            if s <= start < end <= s + r:
                destinations.add((start + offset, end + offset))
                break
            elif s <= start < s + r <= end:
                destinations.add((start + offset, s + r + offset))
                sources.add((s + r, end))
                break
            elif start < s < end <= s + r:
                destinations.add((s + offset, end + offset))
                sources.add((start, s))
                break
        else:
            destinations.add((start, end))

    return destinations


def puzzle9(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    seeds, mappings = parse_input(data)

    sources = set(seeds)
    for mapping in mappings:
        sources = convert(sources, mapping)

    return min(sources)


def puzzle10(input_file: str) -> int:
    data = file_handle.readfile(input_file).strip()
    seeds, mappings = parse_input(data)

    sources = {(s, s + r) for (s, r) in zip(seeds[0::2], seeds[1::2])}
    for mapping in mappings:
        sources = convert_ranges(sources, mapping)

    return min(range_[0] for range_ in sources)


if __name__ == '__main__':
    print('Day #5, part one:', puzzle9('./input/day5.txt'))
    print('Day #5, part two:', puzzle10('./input/day5.txt'))
