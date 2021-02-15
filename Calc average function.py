def find_average(*args):
    av = 0
    for i in args:
        av = av + i

    return print(av / len(args))

find_average(6, 8, 10)