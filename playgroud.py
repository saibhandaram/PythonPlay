def add(*args):
    total = 0
    for n in args:
        total = total + n
    return total


print(add(1, 2, 3, 5))


def cal(**kwargs):
    print(type(kwargs))
    print(kwargs)

cal(add=3 , mul = 10)


def test(*args):
    print(type(args))
    print(args)
test(1, 2, 3, 5)


def all_aboard(a, *args, **kw):
    print(a, args, kw)


    # **kwargs should be after *args
all_aboard(4, 7, 3, 0, x=10, y=64)
