counter = 0


def show_counter():
    print(counter)


def set_counter(c):
    global counter
    counter = c


def set_counter_wo_global(c):
    counter = c


set_counter_wo_global(10)
set_counter(5)
show_counter()
