from functools import reduce


def mod_off(number, mod):
    return min(number, (number - 2) % mod + 2)


def pow_mod(exp, base):
    return mod_off(base, 20) ** mod_off(exp, 4)


def last_digit(lst):
    return reduce(pow_mod, lst[::-1], 1) % 10


if __name__ == "__main__":
    test_data = [
        ([], 1),
        ([0, 0], 1),
        ([0, 0, 0], 0),
        ([1, 2], 1),
        ([3, 4, 5], 1),
        ([4, 3, 6], 4),
        ([7, 6, 21], 1),
        ([12, 30, 21], 6),
        ([2, 2, 2, 0], 4),
        ([937640, 767456, 981242], 0),
        ([123232, 694022, 140249], 6),
        ([499942, 898102, 846073], 6)
    ]
    for test_input, test_output in test_data:
        assert last_digit(test_input) == test_output
