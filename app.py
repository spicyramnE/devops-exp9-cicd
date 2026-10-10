"""Simple application logic used to demonstrate the CI/CD pipeline."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


if __name__ == "__main__":
    print("add(2, 3) =", add(2, 3))
    print("subtract(5, 3) =", subtract(5, 3))
