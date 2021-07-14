a = [1, 2, 3]
print(a)

b = ["teste", "tututi", "tectec"]
print(b)

b[0] = "tuctuc"
print(b)

c = []
c.append(1)
c.append(2)
print(c)

d = [
    "aba",
    "ded",
    "cec",
    "lala",
    "asdsadsa",
    "13aasd",
    "dfs",
    "asdasd",
    "1213sds",
    "asdsad",
]
print(d)

e = list("characters")
print(e)

# second part

ll = [1, -4, 10, 4000, 9]
print(ll[-1])
print(ll[-2])

l3 = [2, 40, 1231, 503, 8892, 91, 23]
print(l3[1:3])
print(l3[1:-1])
print(l3[:2])
print(l3[2:])
print(l3[:])

# copying lists
l3_copy = list(l3)
print(l3_copy is l3)

w = "the quick brown fox jumps over the lazy dog".split()
print(w)
iw = w.index("fox")
print(w[iw])
print(w.count("the"))
print(37 in [1, 2, 3, 40, 38, 39])
print(37 not in [1, 2, 3, 40, 38, 39])

del w[2]
print(" ".join(w))
w.insert(2, "brown")
print(" ".join(w))
w.remove("brown")
print(" ".join(w))


l4 = [1, 2, 3]
l5 = [4, 5, 6]
l6 = l4 + l5
print(l6)
l6 += [7, 8, 9]
print(l6)
l6.extend([12, 11, 10])
print(l6)
l6.reverse()
print(l6)
l6.sort()
print(l6)
l6.sort(reverse=True)
print(l6)


ww = "the quick brown fox jumps over the lazy dog".split()
ww.sort(key=len)
print(ww)
print(" ".join(ww))


xx = [4, 9, 2, 1]
yy = sorted(xx)
print(xx is yy)

pp = [9, 3, 1, 0]
qq = reversed(pp)
print(pp is qq)
print(qq)
print(list(qq))
