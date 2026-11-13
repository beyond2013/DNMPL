"""Problem 55: Tower of Hanoi"""


def p55():
    moves = []

    def hanoi(n, source, target, spare):
        if n == 0:
            return
        hanoi(n - 1, source, spare, target)
        moves.append(f"Move disk {n} from {source} to {target}")
        hanoi(n - 1, spare, target, source)

    hanoi(3, "A", "C", "B")
    print("\n".join(moves))
    print(f"Total moves = {len(moves)} (2^3 - 1)")


if __name__ == "__main__":
    p55()
