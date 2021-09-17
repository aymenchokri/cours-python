def multiplication(*args):
    r=1
    for i in args:
        if type(i) == float:
           r = r * i
        elif type(i) == int:
           r = r * i
        else:
            return print("you must put an integer")

    print(r)


multiplication(2,3,2,1,4.5,5,5.3)
