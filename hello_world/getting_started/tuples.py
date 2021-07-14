t = ("Brazil", "Wagner", 123)

print(t[1])
print(len(t))
print(t + ("Australian", "Kangaroo"))
print(t)

t = t + (
    "Australian",
    "Kangaroo",
    {"Hi": "Hello", "Bye": "Goodbye"},
    ("coffee", "cake", "Toast"),
)

print(len(t))
print(t[5]["Hi"])
print(t[5]["Bye"])
print(t[6][2])
print(t)

tt = 1, 2, 3, 5, 10, 9, 20, 7, 8
print(type(tt))


def minmax(items):
    return min(items), max(items)


print(minmax(tt))


lower, upper = minmax([10, 9, 1, 3, 6, 11, 7, 8, 2])
print(lower, upper)
(a, (b, (c, d))) = (4, (3, (2, 1)))
print(a, b, c, d)
a = "Jelly"
b = "Bean"
a, b = b, a
print(a, b)
l = [1, 2, 3, 4, 5, 6, 7]
tl = tuple(l)
print(tl)
print(5 in tl)
print(5 not in tl)
print(tuple("Wagner"))

