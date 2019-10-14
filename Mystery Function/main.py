def mystery(n):
    return n ^ (n >> 1)


def mystery_inv(n):
    mask = n >> 1
    while mask != 0:
        n = n ^ mask
        mask = mask >> 1
    return n


def name_of_mystery():
    return "Gray code"


if __name__ == "__main__":
    assert mystery(6) == 5
    assert mystery_inv(5) == 6
    assert mystery(9) == 13
    assert mystery_inv(13) == 9
    assert mystery(19) == 26
    assert mystery_inv(26) == 19
