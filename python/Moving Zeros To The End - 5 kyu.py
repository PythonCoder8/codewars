def move_zeros(array):
    count = 0
    for i in array:
        if i == 0:
            count += 1
    array = list(''.join([str(i) for i in array]).replace('0', ''))
    for i in range(count):
        array.append('0')
    return [int(i) for i in array]
