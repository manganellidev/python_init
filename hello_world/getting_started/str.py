str1 = """
0 - Hello,
World!
"""

str2 = "1 - Hello,\nWorld!"

print(str1)

str2 = "1 - Hello,\nWorld!"

print(str2, end="\n\n")

str3 = r"C:\Users\Wagner\Desktop"

print(str3, end="\n\n")

str4 = "parrot"

print(str4[4], end="\n\n")

str5 = "wagner"

print(str5.capitalize())

# second part

print("new" + "found" + "land")
print("".join("new" + "found" + "land"))
print(" ".join(["new", "found", "land"]))
print("_".join(["new", "found", "land"]))

print("unforgetable".partition("forget"))

departure, separator, arrival = "London:Edinburgh".partition(":")
print(departure, separator, arrival)
departure, _, arrival = "London:Edinburgh".partition(":")
print(departure, arrival)


print("The age of {0} is {1}".format("Jim", 5))
print("The age of {0} is {1}. {0}'s birthday is on {2}".format("Jim", 5, "October 31"))
print("The age of {} is {}.".format("Jim", 5))
print("Current position {latitude} {longitude}".format(latitude="60N", longitude="5E"))
print(
    "Galactic position x={pos[0]}, y={pos[1]}, z={pos[2]}".format(
        pos=(65.2, 23.1, 82.2)
    )
)
import math, datetime

print("Math constants: pi={m.pi}, e={m.e}".format(m=math))
print("Math constants: pi={m.pi:.3f}, e={m.e:.3f}".format(m=math))
value = 4 * 20
print("The value is {value}".format(value=value))
print(f"The value is {value}")
print(f"Math constants: pi={math.pi:.3f}, e={math.e:.3f}")
print(f"The current time is {datetime.datetime.now().isoformat()}")
