"""Problem 41: Function — is_prime."""
def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5)+1))

if __name__ == "__main__":
    print(is_prime(17))
