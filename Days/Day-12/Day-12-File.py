
def xPrint_1(input, times):
    prints = 0
    while prints <= times:
        print(input)
        prints = prints + 1

def xPrint_2(input, times):
    for _ in range(times):
        print(input)

xPrint_1("Test1", 5)
xPrint_2("Test2", 5)