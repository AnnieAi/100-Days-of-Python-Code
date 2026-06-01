def add(*args):
    print(args, type(args))
    sum = 0
    for n in args:
        sum += n
    print(sum)

add(1, 3, 4, 6, 7)