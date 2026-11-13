"""Problem 42: Calculator using separate functions."""
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b else None

if __name__ == "__main__":
    print(add(3,4), sub(3,4), mul(3,4), div(3,4))
