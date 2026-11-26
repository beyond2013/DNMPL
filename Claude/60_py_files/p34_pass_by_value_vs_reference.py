"""Problem 34: Pass-by-value vs pass-by-reference behaviour"""


def p34():
    # Python passes object references. Immutable objects (int, str, tuple)
    # behave like pass-by-value; mutable objects (list, dict) can be changed.
    def try_swap_ints(a, b):
        a, b = b, a            # only changes local names

    def swap_in_list(lst):
        lst[0], lst[1] = lst[1], lst[0]   # mutates the caller's list

    def swap_returning(a, b):
        return b, a

    x, y = 1, 2
    try_swap_ints(x, y)
    print("After try_swap_ints:", x, y, "(unchanged)")

    pair = [1, 2]
    swap_in_list(pair)
    print("After swap_in_list :", pair, "(changed)")

    x, y = swap_returning(x, y)
    print("After swap_returning:", x, y, "(idiomatic Python)")


if __name__ == "__main__":
    p34()
