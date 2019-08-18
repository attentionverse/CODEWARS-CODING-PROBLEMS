import time


class Cell:
    def __init__(self, base: int):
        self.base = base
        self.current = base

    def increment(self):
        self.current += self.base

    def __repr__(self):
        return '<Cell base={}, current={}>'.format(self.base, self.current)


class CellsBag:
    def __init__(self, cells):
        self.cells_dict = {}
        for c in cells:
            self.append_cell(c)

    def check_num(self, num):
        # print('check_num {} in cells {}'.format(num, self.cells_dict))
        if num-1 in self.cells_dict:
            self.increment_cell(num-1)
        if num-2 in self.cells_dict:
            self.increment_cell(num-2)
        if num in self.cells_dict:
            self.increment_cell(num)
            return True
        self.append_cell(Cell(num))

        return False

    def get_cells(self, num):
        return self.cells_dict[num]

    def increment_cell(self, num):
        # print('increment {} in cells {}'.format(num, self.cells_dict))
        cells = self.get_cells(num)
        # self.delete_cells(num)
        for cell in cells:
            cell.increment()
            self.append_cell(cell)
        # print('incremented {} in cells {}'.format(num, self.cells_dict))

    def append_cell(self, cell):
        if cell.current in self.cells_dict:
            self.cells_dict[cell.current].append(cell)
        else:
            self.cells_dict[cell.current] = [cell]

    def delete_cells(self, num):
        del self.cells_dict[num]


class Primes:
    @staticmethod
    def stream():
        yield 2
        num_to_check = 3
        cells_bag = CellsBag([])
        while True:
            checked = Primes.check_cells(num_to_check, cells_bag)
            if checked:
                yield num_to_check

            num_to_check += 2

    @staticmethod
    def check_cells(num, cells_bag):
        if cells_bag.check_num(num):
            return False

        return True


if __name__ == "__main__":
    start = time.time()

    primes_gen = Primes.stream()

    for i in range(1000000):
        next_prime = next(primes_gen)
        # print('{}'.format(next_prime))
        if i % 50000 == 0:
            end = time.time()
            print('{}: {} – {}'.format(end - start, i, next_prime))

    # def verify(from_n, *vals):
    #     stream = Primes.stream()
    #     for _ in range(from_n):
    #         next(stream)
    #     for v in vals:
    #         assert next(stream) == v
    #
    # verify(0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
    # verify(10, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71)
    # verify(100, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601)
    # verify(1000, 7927, 7933, 7937, 7949, 7951, 7963, 7993, 8009, 8011, 8017)
