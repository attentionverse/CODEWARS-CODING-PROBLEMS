import math


def snail(inp):
    if inp[0] == []:
        return []

    out = []
    size = len(inp)
    layers_num = math.ceil(size / 2)

    for l in range(0, layers_num):
        # top horizontal edge / left to right
        edge_len = size - l*2
        if edge_len:
            x0 = 0 + l
            y0 = 0 + l
            xn = x0 + edge_len - 1
            for x in range(x0, xn + 1):
                if y0 < size and x < size:
                    out.append(inp[y0][x])

        # right vertical edge / up to down
        edge_len = size - l*2 - 1
        if edge_len:
            x0 = size - l - 1
            y0 = l + 1
            yn = y0 + edge_len - 1
            for y in range(y0, yn + 1):
                if x0 < size and y < size:
                    out.append(inp[y][x0])

        # bottom horizontal edge / right to left
        edge_len = size - l*2 - 1
        if edge_len:
            x0 = size - (l+1) - 1
            y0 = size - l - 1
            xn = l
            for x in range(x0, xn - 1, -1):
                if y0 < size and x < size:
                    out.append(inp[y0][x])

        # left vertical edge / down to up
        edge_len = size - (l+1)*2
        if edge_len:
            x0 = l
            y0 = size - (l+1) - 1
            yn = y0 - (edge_len - 1)
            for y in range(y0, yn - 1, -1):
                if y < size and x0 < size:
                    out.append(inp[y][x0])

    [print(_) for _ in out]

    return out


if __name__ == "__main__":
    for assert_input in [
        [
            [[1, 2, 3, 4, 5],
             [6, 7, 8, 9, 10],
             [11, 12, 13, 14, 15],
             [16, 17, 18, 19, 20],
             [21, 22, 23, 24, 25]],
            [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]
        ],
        [
            [[]], []
        ],
        [
            [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]],
            [1, 2, 3, 6, 9, 8, 7, 4, 5]
        ],
        [
            [[1, 2, 3],
             [8, 9, 4],
             [7, 6, 5]],
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ],
    ]:
        print('assert_input: {}'.format(assert_input))
        assert (snail(assert_input[0]) == assert_input[1])
