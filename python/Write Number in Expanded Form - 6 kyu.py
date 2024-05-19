def expanded_form(num):
    factor = 1
    stmt = ""
    my_list = []
    for i in list(str(num))[::-1]:
        if int(i) != 0:
            my_list.append(str(int(i) * factor))
        factor *= 10
    return " + ".join(my_list[::-1])
