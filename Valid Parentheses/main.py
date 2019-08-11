def valid_parentheses(string):
    is_valid = True

    brackets_stack = 0
    for i in string:
        if i == '(':
            brackets_stack += 1
        if i == ')':
            brackets_stack -= 1
            if brackets_stack < 0:
                is_valid = False
                break

    if brackets_stack != 0:
        is_valid = False

    return is_valid


if __name__ == "__main__":
    for assert_input in [
        ["()", True],
        [")(()))", False],
        ["(", False],
        ["(())((()())())", True],
        ["  (", False],
        [")test", False],
        ["", True],
        ["hi())(", False],
        ["hi(hi)()", True],
    ]:
        print('assert_input: {}'.format(assert_input))
        assert (valid_parentheses(assert_input[0]) == assert_input[1])
