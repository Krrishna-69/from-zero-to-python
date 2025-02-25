def sum_all(*args):
    print(args)
    for i in args:
        print(i*2)
    return sum(args)

print(sum_all(1, 3))
# print(sum_all(1, 3, 5))
# print(sum_all(1, 3, 6, 9))
