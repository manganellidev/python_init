a = "Hello Wagner, how are you?"

b = a.encode("utf-8")

print(b)

aa = b.decode("utf-8")

print(aa)

print(a == aa)
