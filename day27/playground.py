
def add(*args):
    sum = 0
    for i in args:
        sum += i

    return sum

x = add(1, 2, 7, 9)
print(x)