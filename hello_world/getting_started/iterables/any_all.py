print(any([False, False, True]))

print(all([True, True, True]))

from math import sqrt


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


print(any(is_prime(x) for x in range(1328, 1361)))

print(
    all(
        name == name.title()
        for name in ["London", "Paris", "Tokyo", "New York", "Sydney"]
    )
)
