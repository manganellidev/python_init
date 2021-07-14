def gen123():
    yield 1
    yield 2
    yield 3


g = gen123()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))  # error StopIteration


def gen246():
    print("yield 2")
    yield 2
    print("yield 4")
    yield 4
    print("yield 6")
    yield 6


g = gen246()

# while True:
#     try:
#         print(next(g))
#     except StopIteration:
#         pass


def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def run_pipeline():
    items = [3, 6, 6, 2, 1, 1]
    for item in take(3, list(distinct(items))):
        print(item)


# run_pipeline()


# Generator expression
# (expr(item) for item in iterable)

thousand_squares = (x * x for x in range(1, 1001))
print(thousand_squares)
print(list(thousand_squares)[-10:])
print(list(thousand_squares))
t = (x * x for x in range(1, 1001))
print(list(t)[-10:])


# Generator expression with func
# func(expr(item) for item in iterable)

print(sum(x * x for x in range(1, 10000001)))

from math import sqrt


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


print(sum(x for x in range(1001) if is_prime(x)))
