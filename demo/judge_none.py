def test():
    if value == 1:
        a = b = 1
        return a, b


value = 0
a = test()
if a is None:
    print("test none")
else:
    a,b = test()
    print('right, a,b is',a,b )
# a, b = test()