import time


cache_inner_shifts = {}
cache_outer_shifts = {}


def periods_sequence(initial_step, size):
    i = initial_step
    while True:
        steps = yield [i, i + size]
        i += (size+1)*steps if steps else size+1


def get_overlap(period_a, period_b):
    left = max(period_a[0], period_b[0])
    right = min(period_a[1], period_b[1])
    if left <= right:
        return [left, right]
    else:
        return None


def spinning_rings(inner_max, outer_max):
    time_start = time.time()
    print('inner_max={}, outer_max={}'.format(inner_max, outer_max))
    global cache_inner_shifts, cache_outer_shifts
    cache_inner_shifts = {}
    cache_outer_shifts = {}

    seq_a = periods_sequence(1, inner_max)
    seq_b = periods_sequence(0, outer_max)

    period_a = next(seq_a)
    period_b = next(seq_b)

    while period_a[1] - period_b[1] > (period_b[1] - period_b[0] + 1):
        steps_to_move = (period_a[1] - period_b[1]) // (period_b[1] - period_b[0] + 1)
        steps_to_move = steps_to_move if steps_to_move else 1
        period_b = seq_b.send(steps_to_move)
    while period_a[0] - period_b[0] > (period_a[1] - period_a[0] + 1) \
            and period_b[1] - period_a[1] > (period_a[1] - period_a[0] + 1):
        steps_to_move = (period_b[1] - period_a[1]) // (period_a[1] - period_a[0] + 1)
        steps_to_move = steps_to_move if steps_to_move else 1
        period_a = seq_a.send(steps_to_move)

    overlaps_checked = 0
    while True:
        # print('period_a: {}'.format(period_a))
        # print('period_b: {}'.format(period_b))
        overlap = get_overlap(period_a, period_b)
        if overlap:
            overlaps_checked += 1

            # print('overlap: {}'.format(overlap))
            if overlap[0] not in cache_inner_shifts:
                cache_inner_shifts[overlap[0]] = (overlap[0] // (inner_max + 1)) + 1 \
                    if overlap[0] % (inner_max + 1) > 0 else int(overlap[0] / (inner_max + 1))
            inner_shift = cache_inner_shifts[overlap[0]]
            # print('inner_shift: {}'.format(inner_shift))
            # inner: y = -x + inner_shift*(inner_max+1)
            # print('inner: y = -x + {}*({}+1)'.format(inner_shift, inner_max))

            if overlap[0] not in cache_outer_shifts:
                cache_outer_shifts[overlap[0]] = overlap[0] // (outer_max + 1) + 1
            outer_shift = cache_outer_shifts[overlap[0]]
            # print('outer_shift: {}'.format(outer_shift))
            # outer: y = x - (outer_shift-1)*(outer_max+1)
            # print('outer: y = x - ({}-1)*({}+1)'.format(outer_shift, outer_max))

            # x - (outer_shift-1)*(outer_max+1) = -x + inner_shift*(inner_max+1)
            # 2x = inner_shift*(inner_max+1) + (outer_shift-1)*(outer_max+1)
            # x = (inner_shift*(inner_max+1) + (outer_shift-1)*(outer_max+1)) / 2

            step_eq = (inner_shift * (inner_max + 1) + (outer_shift-1)*(outer_max+1)) / 2
            if step_eq % 1 == 0 and overlap[0] <= step_eq <= overlap[1]:
                step_eq = int(step_eq)
                print('step_eq: {}'.format(step_eq))
                print('overlaps_checked: {}'.format(overlaps_checked))
                print('{}'.format(time.time() - time_start))

                return step_eq

        if period_a[1] <= period_b[1]:
            period_a = next(seq_a)
        else:
            period_b = next(seq_b)

        while period_a[1] - period_b[1] > (period_b[1] - period_b[0] + 1):
            steps_to_move = (period_a[1] - period_b[1]) // (period_b[1] - period_b[0] + 1)
            steps_to_move = steps_to_move if steps_to_move else 1
            period_b = seq_b.send(steps_to_move)
        while period_a[0] - period_b[0] > (period_a[1] - period_a[0] + 1) \
                and period_b[1] - period_a[1] > (period_a[1] - period_a[0]+1):
            steps_to_move = (period_b[1] - period_a[1]) // (period_a[1] - period_a[0] + 1)
            steps_to_move = steps_to_move if steps_to_move else 1
            period_a = seq_a.send(steps_to_move)


if __name__ == "__main__":
    assert spinning_rings(2, 2) == 3
    assert spinning_rings(176, 8145) == 8321
    assert spinning_rings(9736, 49) == 19437
    assert spinning_rings(2 ** 24, 3 ** 15) == 23951671  # 16777216, 14348907
    # # LCM 240 734 712 102 912
    assert spinning_rings(16, 5) == 29
    assert spinning_rings(17, 5) == 15
    assert spinning_rings(1, 1) == 1
    assert spinning_rings(3, 3) == 2
    assert spinning_rings(2, 3) == 5
    assert spinning_rings(3, 2) == 2
    assert spinning_rings(5, 5) == 3
    assert spinning_rings(7, 9) == 4
    assert spinning_rings(2, 10) == 13
