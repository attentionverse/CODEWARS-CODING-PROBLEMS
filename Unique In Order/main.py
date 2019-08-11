from typing import List


def unique_in_order(iterable) -> List:
    out = []
    for i, v in enumerate(iterable):
        if i == 0:
            out.append(v)
            continue

        if v != iterable[i-1]:
            out.append(v)
            continue

    return out


if __name__ == "__main__":
    for assert_input in [
        ['AAAABBBCCDAABBB', ['A', 'B', 'C', 'D', 'A', 'B']],
        ['ABBCcAD', ['A', 'B', 'C', 'c', 'A', 'D']],
        [[1, 2, 2, 3, 3], [1, 2, 3]]
    ]:
        print('assert_input: {}'.format(assert_input))
        assert (unique_in_order(assert_input[0]) == assert_input[1])
