def spinning_rings(inner_max, outer_max):
    print('inner_max={}, outer_max={}'.format(inner_max, outer_max))

    def outer_generator(outer_max):
        current = 1
        while True:
            yield current
            current = 0 if current == outer_max else current + 1

    def inner_generator(inner_max):
        current = inner_max
        while True:
            yield current
            current = inner_max if current == 0 else current - 1

    outer_gen = outer_generator(outer_max)
    inner_gen = inner_generator(inner_max)

    step = 1
    while True:
        next_outer_gen = next(outer_gen)
        next_inner_gen = next(inner_gen)
        print('{}: next_outer_gen={}, next_inner_gen={}'.format(step, next_outer_gen, next_inner_gen))
        if next_outer_gen == next_inner_gen:
            return step
        step += 1


if __name__ == "__main__":
    assert spinning_rings(1, 1) == 1
    assert spinning_rings(16, 5) == 29
    assert spinning_rings(17, 5) == 15
    assert spinning_rings(3, 3) == 2
    assert spinning_rings(2, 3) == 5
    assert spinning_rings(3, 2) == 2
    assert spinning_rings(2, 2) == 3
