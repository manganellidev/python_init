p = {1, 1231, 7453, 9, 22, 405}
print(type(p))

d = {}
print(type(d))

e = set()
print(type(e))

s = set([1, 3, 102, 32, 43, 12, 1023, 40])
print(s)
t = [1, 3, 10, 12, 4]
print(set(t))

print(102 in s)
print(102 not in s)

s.add(41)
print(s)
s.update({41, 42, 43, 44, 45})
print(s)

s.remove(41)
print(s)

ss = set(s)
print(ss is s)

blue_eyes = {"Olivia", "Harry", "Lily", "Jack", "Amelia"}
blond_hair = {"Harry", "Jack", "Amelia", "Mia", "Joshua"}
smell_hcn = {"Harry", "Amelia"}
taste_ptc = {"Harry", "Amelia"}
o_blood = {"Mia", "Joshua", "Lily", "Olivia"}
b_blood = {"Amelia", "Jack"}
a_blood = {"Harry"}
ab_blood = {"Joshua", "Lola"}
print(blue_eyes.union(blond_hair))
print(blue_eyes.union(blond_hair) == blond_hair.union(blue_eyes))
print(blue_eyes.intersection(blond_hair))
print(blue_eyes.intersection(blond_hair) == blond_hair.intersection(blue_eyes))
print(blue_eyes.difference(blond_hair))
print(blond_hair.difference(blue_eyes))
print(blond_hair.symmetric_difference(blue_eyes))
print(blond_hair.symmetric_difference(blue_eyes) == blue_eyes.symmetric_difference(blond_hair))
print(smell_hcn.issubset(blond_hair))
print(taste_ptc.issuperset(smell_hcn))
print(a_blood.isdisjoint(o_blood))
