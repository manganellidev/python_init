sunday = [14, 16, 20, 18, 30, 20, 22, 16, 15, 11]
monday = [19, 20, 21, 15, 17, 22, 30, 11, 14, 12]
tuesday = [22, 30, 11, 22, 16, 19, 12, 30, 11, 15]

# for item in zip(sunday, monday, tuesday):
#     print(item)

# for sun, mon, tue in zip(sunday, monday, tuesday):
#     print(f"average = {(sun + mon + tue) / 3:.2f}")

for temps in zip(sunday, monday, tuesday):
    print(
        f"min={min(temps):4.1f}, max={max(temps):4.1f}, average={sum(temps) / len(temps):4.1f}"
    )

print(sum(sun + mon + tue for sun, mon, tue in zip(sunday, monday, tuesday)))

from itertools import chain

temperatures = chain(sunday, monday, tuesday)
print(all(t > 0 for t in temperatures))
