a = {"Wagner": "99339", "Anaysa": "99637", "Leopoldo": "123"}
print(a)
print(a["Wagner"])

a["Tuctuc"] = "98312"
print(a)

# second part

names_and_ages = [("Wagner", 27), ("Anaysa", 25), ("Tuctuc", 1)]
d = dict(names_and_ages)
print(d)
phonetic = dict(a="alfa", b="beta", c="charlie")
print(phonetic)

p_copy = phonetic.copy()
print(p_copy)
print(p_copy is phonetic)
p_copy2 = dict(phonetic)
print(p_copy2)
print(p_copy2 is phonetic)

phonetic.update({"d": "delta"})
print(phonetic)
stocks = {"GOOG": 894, "AAPL": 416, "IBM": 194}
stocks.update({"GOOG": 1000, "YHOO": 25})
print(stocks)

for key in stocks:
    print(f"{key} => {stocks[key]}")
for value in stocks.values():
    print(value)
for key in stocks.keys():
    print(key)
for key, value in stocks.items():
    print(f"{key} => {value}")

print("GOOG" in stocks)
print("GOOG" not in stocks)
del stocks["GOOG"]
print(stocks)
print("GOOG" in stocks)
stocks["AAPL"] = 417
print(stocks)

from pprint import pprint as pp

stocks.update({"GOOG": 1002, "F": 40, "GM": 25, "AAAASSS": 12345})
pp(stocks)
