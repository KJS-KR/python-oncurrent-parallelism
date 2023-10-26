def outer_func_01():
    a = 20

    def inner_func():
        a = 30
        print("a = %d" % a)

    inner_func()
    print("a = %d" % a)


a = 10
outer_func_01()
print("a = %d" % a)


def outer_func_02():
    a = 20

    def inner_func():
        a = 30
        print(locals())

    inner_func()
    print(locals())


a = 10
outer_func_02()
print(locals())


def outer_func_03():
    a = 20

    def inner_func():
        a = 30

    inner_func()


a = 10
outer_func_03()
print(locals())
print(globals())
