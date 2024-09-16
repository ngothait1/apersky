# 1.
def addItem(my_list, item):
    my_list.append(item)


def sortRegular():
    the_list = [29, 23, 23, 65, 29, 43, 61, 81, 93, 10, 10, 10, 97, 78, 38, 66, 60, 55, 22, 70]
    the_list.sort()
    print(the_list)


def sortReverse():
    the_list = [29, 23, 23, 65, 29, 43, 61, 81, 93, 10, 10, 10, 97, 78, 38, 66, 60, 55, 22, 70]
    the_list.sort(reverse=True)
    print(the_list)


def printTheBiggerNum():
    the_list = [29, 23, 23, 65, 29, 43, 61, 81, 93, 10, 10, 10, 97, 78, 38, 66, 60, 55, 22, 70]
    print(max(the_list))


def printTheSmallNum():
    the_list = [29, 23, 23, 65, 29, 43, 61, 81, 93, 10, 10, 10, 97, 78, 38, 66, 60, 55, 22, 70]
    print(min(the_list))


def printBig5():
    the_list = [29, 23, 23, 65, 29, 43, 61, 81, 93, 10, 10, 10, 97, 78, 38, 66, 60, 55, 22, 70]
    the_list.sort()
    print(the_list[-5:])


def orderTheList():
    a_messy_list = "16|11|20|-2|9|19|7|5|10|5|20|-9|16|7|4|2|-5|2|-3|10"
    good_list = a_messy_list.split("|")
    good_list.sort()
    print(good_list)


# 2.a
sortRegular()
# 2.b
sortReverse()
# 2.c
printTheBiggerNum()
# 2.d
printTheSmallNum()
# 2.e
printBig5()
# 3.
orderTheList()