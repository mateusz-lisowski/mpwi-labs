def generate_variations_with_repeats(input_list: list, length: int) -> list[list]:

    if length == 0:
        return [[]]

    variations: list[list] = []
    for element in input_list:
        sub_variations = generate_variations_with_repeats(input_list, length - 1)
        for sub_variation in sub_variations:
            variations.append([element] + sub_variation)

    return variations


def generate_variations_without_repeats(input_list: list, length: int) -> list[list]:

    if length == 0:
        return [[]]

    variations = []
    for i, element in enumerate(input_list):
        remaining_elements = input_list[:i] + input_list[i+1:]
        sub_variations = generate_variations_without_repeats(remaining_elements, length - 1)
        for sub_variation in sub_variations:
            variations.append([element] + sub_variation)

    return variations


def main():
    pass


if __name__ == '__main__':
    main()
