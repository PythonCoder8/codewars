def find_uniq(arr):
    char_map = {}
    
    for string in arr:
        char_set = frozenset(string.lower())
        if char_set in char_map:
            char_map[char_set].append(string)
        else:
            char_map[char_set] = [string]
            
    for key, value in char_map.items():
        if len(value) == 1:
            return value[0]
