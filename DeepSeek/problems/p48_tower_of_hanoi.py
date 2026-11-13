"""Problem 48: Tower of Hanoi."""
def hanoi(n, src, aux, dst):
    if n == 1:
        print(f"Move disk 1: {src} -> {dst}")
        return
    hanoi(n-1, src, dst, aux)
    print(f"Move disk {n}: {src} -> {dst}")
    hanoi(n-1, aux, src, dst)

if __name__ == "__main__":
    hanoi(3, 'A', 'B', 'C')
