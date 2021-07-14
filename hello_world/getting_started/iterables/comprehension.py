# list/set comprehension syntax
# [ expr(item) for item in iterable ]


words = "Why sometimes I have believed as many as six impossible things before breakfast".split()

print([len(word) for word in words])

from math import factorial

f = [len(str(factorial(x))) for x in range(20)]
print(f)

f_set = {len(str(factorial(x))) for x in range(20)}
print(f_set)


# dict comprehension syntax
# [ expr(item): value_expr(item) for item in iterable ]
country_to_capital = {
    "United Kingdom": "London",
    "Brazil": "Brasília",
    "Morocco": "Rabat",
    "Sweden": "Stockholm",
}
capital_to_country = {
    capital: country for country, capital in country_to_capital.items()
}
from pprint import pprint as pp

pp(capital_to_country)

words = ["hi", "hello", "foxtrot", "hotel"]
w_dic = {x[0]: x for x in words}
print(w_dic)


import os
import glob

file_sizes = {
    os.path.realpath(file): os.stat(file).st_size for file in glob.glob("*.py")
}
pp(file_sizes)


from math import sqrt


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


print([x for x in range(101) if is_prime(x)])
prime_square_divisors = {x * x: (1, x, x * x) for x in range(100) if is_prime(x)}
pp(prime_square_divisors)


def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("Iterable is empty.")


print(first(["1st", "2nd", "3rd"]))
print(first({"1st", "2nd", "3rd"}))
print(first(set()))
