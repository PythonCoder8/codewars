def snail(array):
    snail_array = []
    while len(array) > 0:
        snail_array += array[0]
        del array[0]
        if len(array) > 0:
            for i in array:
                snail_array += [i[-1]]
                del i[-1]
            if array[-1]:
                snail_array += array[-1][::-1]
                del array[-1]
            for i in array[::-1]:
                snail_array += [i[0]]
                del i[0]
    return snail_array
