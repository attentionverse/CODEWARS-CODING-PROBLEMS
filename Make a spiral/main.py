import math


def spiralize(size):
    default_val = 4
    out = [[default_val for _ in range(size)] for _ in range(size)]
    layers_num = math.ceil(size / 4)

    for l in range(0, layers_num):
        # top horizontal edge / left to right
        edge_len = size - l * 4
        if edge_len:
            x0 = 0 + l*2
            y0 = 0 + l*2
            xn = x0 + edge_len - 1
            y1 = y0
            y2 = y0 + 1
            for x in range(x0, xn + 1):
                if y1 < size and x < size:
                    if out[y1][x] == default_val:
                        out[y1][x] = 1
                if y2 < size and x < size:
                    if out[y2][x] == default_val:
                        out[y2][x] = 0 if x < xn else 1

        # right vertical edge / up to down
        edge_len = size - l*4 - 2
        if edge_len:
            x0 = size - l*2 - 1
            y0 = 0 + (l+1)*2
            yn = y0 + edge_len - 1
            x1 = x0
            x2 = x0 - 1
            for y in range(y0, yn + 1):
                if x1 < size and y < size:
                    if out[y][x1] == default_val:
                        out[y][x1] = 1
                if x2 < size and y < size:
                    if out[y][x2] == default_val:
                        out[y][x2] = 0 if y < yn else 1

        # bottom horizontal edge / right to left
        edge_len = size - l * 4
        if edge_len:
            x0 = size - (l+1)*2 - 1
            y0 = size - l*2 - 1
            xn = l*2
            y1 = y0
            y2 = y0 - 1
            for x in range(x0, xn - 1, -1):
                if y1 < size and x < size:
                    if out[y1][x] == default_val:
                        out[y1][x] = 1
                if y2 < size and x < size:
                    if out[y2][x] == default_val:
                        out[y2][x] = 0 if x > xn else 1

        # left vertical edge / down to up
        edge_len = size - (l+1)*4
        if edge_len:
            x0 = l*2
            y0 = size - (l+1)*2 - 1
            yn = y0 - edge_len
            x1 = x0
            x2 = x0 + 1
            for y in range(y0, yn - 1, -1):
                if y < size and x1 < size:
                    if out[y][x1] == default_val:
                        out[y][x1] = 1
                if y < size and x2 < size:
                    if out[y][x2] == default_val:
                        out[y][x2] = 0 if y > yn + 1 else 1

    # [print(_) for _ in out]
    spiral = out
    return spiral


if __name__ == "__main__":
    for assert_input in [
        [0, []],
        [
            10,
            [
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
                [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            ]
        ],
        [
            1,
            [[1]]
        ],
        [
            2,
            [
                [1, 1],
                [0, 1]
            ]
        ],
        [
            3,
            [
                [1, 1, 1],
                [0, 0, 1],
                [1, 1, 1]
            ]
        ],
        [
            5,
            [
                [1, 1, 1, 1, 1],
                [0, 0, 0, 0, 1],
                [1, 1, 1, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1]
            ]
        ],
        [
            8,
            [
                [1, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 0, 1],
                [1, 0, 0, 0, 0, 1, 0, 1],
                [1, 0, 1, 0, 0, 1, 0, 1],
                [1, 0, 1, 1, 1, 1, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1]
            ]
        ]
    ]:
        print('assert_input: {}'.format(assert_input))
        assert (spiralize(assert_input[0]) == assert_input[1])
