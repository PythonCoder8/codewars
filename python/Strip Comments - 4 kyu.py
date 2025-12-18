def strip_comments(strng, markers):
    lines = strng.split("\n")
    list_pos = 0
    for line in lines:
        str_pos = 0
        for c in line:
            if c in markers:
                lines[list_pos] = lines[list_pos][:str_pos].rstrip()
            str_pos += 1
        list_pos += 1
    return "\n".join(lines)
