def greet():
    a=20
    def greet1():
        nonlocal a
        print(a)
        a=30
        def greet2():
            nonlocal a
            print(a)
        greet2()
    greet1()
    print(a)
greet()
    