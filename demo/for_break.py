for x in range(10):
    for a in range(3):
        if a != 1 and a!=2:
            continue
        print('***************', x, a)
    print('..............', x, a)