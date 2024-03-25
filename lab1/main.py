import csv
import math
from dataclasses import dataclass


@dataclass
class City:

    name: str
    population: int
    lat: float
    lng: float

    @staticmethod
    def calculate_route_length(cities: list['City']) -> float:
        length = 0.0
        for i in range(len(cities) - 1):
            curr = cities[i]
            nxt = cities[i + 1]
            length += curr.calculate_distance(nxt)
        return length

    def calculate_distance(self, other: 'City') -> float:
        return math.sqrt(math.pow(self.lat - other.lat, 2) + math.pow(self.lng - other.lng, 2))


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

    variations: list[list] = []
    for i, element in enumerate(input_list):
        remaining_elements = input_list[:i] + input_list[i+1:]
        sub_variations = generate_variations_without_repeats(remaining_elements, length - 1)
        for sub_variation in sub_variations:
            variations.append([element] + sub_variation)

    return variations


def calculate_variation_with_repeats(number_of_elements: int, number_of_chosen: int) -> int:
    return int(math.factorial(number_of_elements) / math.factorial(number_of_elements - number_of_chosen))


def calculate_variations_without_repeats(number_of_elements: int, number_of_chosen: int) -> int:
    return pow(number_of_elements, number_of_chosen)


def order_variations(variations: list[list]) -> list[list]:
    variations = variations[:]
    variations = list(map(lambda li: sorted(li), variations))
    output: list[list] = []
    for var in variations:
        if var not in output:
            output.append(var)
    return output


def main():

    data = csv.reader()

    max_number = int(input("Enter maximal number: "))
    size = int(input("Enter size of the variation: "))

    print("\nVariations without repeats")
    variations_without_reps = generate_variations_without_repeats(list(range(1, max_number + 1)), size)
    variations_without_reps_unique = order_variations(variations_without_reps)
    for index, var in enumerate(variations_without_reps_unique):
        print(f"{index + 1}: {var}")

    print(f"There should be {calculate_variation_with_repeats(max_number, size)} variations")

    print("\nVariations with repeats")
    variations_reps = generate_variations_with_repeats(list(range(1, max_number + 1)), size)
    variations_reps_unique = order_variations(variations_reps)
    for index, var in enumerate(variations_reps_unique):
        print(f"{index + 1}: {var}")

    print(f"There should be {calculate_variations_without_repeats(max_number, size)} variations")


if __name__ == '__main__':
    main()
