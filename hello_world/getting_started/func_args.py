def banner(message, border="-"):
    line = border * len(message)
    print(line)
    print(message)
    print(line)


banner("I'm Sr. Poldo")


def add_spam(menu=[]):
    menu.append("spam")
    return menu


print(add_spam(["potato"]))
print(add_spam(["potato"]))
print(add_spam(["potato"]))

print(add_spam())
print(add_spam())
print(add_spam())


def add_spam_fixed(menu=None):
    if menu is None:
        menu = []
    menu.append("spam")
    return menu


print(add_spam_fixed(["potato"]))
print(add_spam_fixed(["potato"]))
print(add_spam_fixed(["potato"]))

print(add_spam_fixed())
print(add_spam_fixed())
print(add_spam_fixed())
