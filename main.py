def generate_variations_with_repeats(input_list: list, length: int) -> list[list]:

    if length == 0:
        return [[]]

    variations: list[list] = []
    for element in input_list:
        sub_variations = generate_variations_with_repeats(input_list, length - 1)
        for sub_variation in sub_variations:
            variations.append([element] + sub_variation)

    return variations


def main():
    res1 = generate_variations_with_repeats([1, 2, 3], 3)
    print(res1)

if __name__ == '__main__':
    main()
