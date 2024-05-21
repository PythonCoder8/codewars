def first_non_repeating_letter(string):
    count = 0
    for i, j in zip(string.lower(), string):
        if string.lower().count(i) == 1:
            count += 1
            return i.upper() if string.find(i) == -1 else i.lower()
    if count == 0:
        return ''
