a = 10
b = 20
def test():
    count = sum([a, b])  # sum expects an iterable, like a list
    print(count)
    return count

test()