def unique_in_order(strline):
    prev = ""
    response = []
    for x in range(0, len(strline)):
        if strline[x] != prev:
            prev = strline[x]
            response.append(strline[x])

    return response
