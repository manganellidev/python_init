a = 123

b = a

print(b is a)

a = 555

print(b is a)

c = [1, 2, 3]

d = c

print(c is d)

d[1] = 10

print(c is d)
print(d, c)
# the list is equal for both c and d.
# there is only a link (reference) between the var names and the list values

bbb = ["a", "b", "c"]


def aaa(bbb):
    return bbb


ccc = aaa(bbb)
print(ccc is bbb)
print(ccc)


bbb = ["a", "b", "c"]


def aaa_copy(bbb):
    aux = []
    for i in bbb:
        aux.append(i)
    return aux


ccc = aaa_copy(bbb)
print(ccc is bbb)
print(ccc)
