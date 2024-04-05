def xor(n1: int, n2: int) -> int:
    if n1 == n2:
        return 0
    return 1


def calculate_bits(bits: list[int]) -> list[int]:
    numbers: list[int] = []
    while len(bits) > 32:
        bits_chunk = bits[len(bits) - 32:]

        result = 0
        for index, number in enumerate(reversed(bits_chunk)):
            if index == 31:
                break
            result += (2 * number) ** index

        numbers.append(result)
        for _ in range(32):
            bits.pop()
    return numbers


def generate_bits(num_cap: int = 31) -> list[int]:
    start_bits = [1, 0, 0, 1, 1, 0, 1]
    i = len(start_bits)
    while len(start_bits) <= num_cap:
        new_bit = xor(start_bits[i - 7], start_bits[i - 3])
        start_bits.append(new_bit)
        i += 1
    return start_bits


def generate_number(cap: int = 1, seed: int = 15, a: int = 69069, constant: int = 1) -> int:
    return (a * seed + constant) % cap


def main():

    cap = 2 ** 31 - 1
    limit = 100_000

    numbers: list[int] = []
    prev = 15
    for _ in range(limit):
        new_number = generate_number(cap=cap, seed=prev)
        numbers.append(new_number)
        prev = new_number

    groups = [0 for _ in range(10)]
    for number in numbers:
        group_index = int(number * 10 / cap)
        groups[group_index] += 1

    print(groups)

    bits = generate_bits(32 * limit)
    bits_numbers = calculate_bits(bits)

    groups = [0 for _ in range(10)]
    for number in bits_numbers:
        group_index = int(number * 10 / cap)
        groups[group_index] += 1

    print(groups)


if __name__ == '__main__':
    main()
