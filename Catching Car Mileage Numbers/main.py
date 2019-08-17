def check_number(number, awesome_phrases):
    if number < 100:
        return False

    # Any digit followed by all zeros: 100, 90000
    digits = [int(_) for _ in str(number)]
    if digits[0] > 0 and sum(_ for _ in digits[1:]) == 0:
        print('{} – Any digit followed by all zeros'.format(number))
        return True

    # Every digit is the same number: 1111
    digits_set = set(digits)
    if len(digits_set) == 1:
        print('{} – Every digit is the same number'.format(number))
        return True

    # The digits are sequential, incementing†: 1234
    if digits[0] <= (11 - len(digits)) and len(digits) <= 10:
        is_sequential_incementing = True
        for i in range(1, len(digits)):
            if not (digits[i] == digits[i-1]+1 or (digits[i] == 0 and digits[i-1] == 9)):
                is_sequential_incementing = False
        if is_sequential_incementing:
            print('{} – The digits are sequential, incementing'.format(number))
            return True

    # The digits are sequential, decrementing‡: 4321
    if digits[0] >= len(digits)-1 and len(digits) <= 10:
        is_sequential_decrementing = True
        for i in range(1, len(digits)):
            if not (digits[i]+1 == digits[i-1] or (digits[i] == 9 and digits[i-1] == 0)):
                is_sequential_decrementing = False
        if is_sequential_decrementing:
            print('{} – The digits are sequential, decrementing'.format(number))
            return True

    # The digits are a palindrome: 1221 or 73837
    half_len = len(digits) // 2
    is_palindrome = True
    for i in range(half_len):
        if digits[i] != digits[len(digits) - 1 - i]:
            is_palindrome = False
    if is_palindrome:
        print('{} – The digits are a palindrome'.format(number))
        return True

    # The digits match one of the values in the awesome_phrases array
    if number in awesome_phrases:
        print('{} – The digits match one of the values in the awesome_phrases array'.format(number))
        return True

    return False


def is_interesting(number, awesome_phrases):
    is_this_interesting = check_number(number, awesome_phrases)
    if is_this_interesting:
        return 2

    is_second_interesting = check_number(number+1, awesome_phrases)
    if is_second_interesting:
        return 1

    is_third_interesting = check_number(number+2, awesome_phrases)
    if is_third_interesting:
        return 1

    return 0


if __name__ == "__main__":
    tests = [
        {'n': 120, 'interesting': [], 'expected': 1},
        {'n': 7382, 'interesting': [], 'expected': 0},
        {'n': 7540, 'interesting': [], 'expected': 0},
        {'n': 1590, 'interesting': [], 'expected': 0},
        {'n': 7473747, 'interesting': [], 'expected': 2},
        {'n': 67890, 'interesting': [], 'expected': 2},
        {'n': 234567890, 'interesting': [], 'expected': 2},
        {'n': 3210, 'interesting': [], 'expected': 2},
        {'n': 3, 'interesting': [1337, 256], 'expected': 0},
        {'n': 1336, 'interesting': [1337, 256], 'expected': 1},
        {'n': 1337, 'interesting': [1337, 256], 'expected': 2},
        {'n': 11208, 'interesting': [1337, 256], 'expected': 0},
        {'n': 11209, 'interesting': [1337, 256], 'expected': 1},
        {'n': 11211, 'interesting': [1337, 256], 'expected': 2},
    ]
    for t in tests:
        print('assert_input: {}, {}'.format(t['n'], t['interesting']))
        print('assert_expexted: {}'.format(t['expected']))
        assert is_interesting(t['n'], t['interesting']) == t['expected']
