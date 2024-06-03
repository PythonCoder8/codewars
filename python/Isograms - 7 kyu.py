def is_isogram(string):
    
    #same case for case insensitivity
    lower_string = string.lower()
    
    #chars we have seen
    chars = []
    
    for i in lower_string:
        
        #checking if we have iterated
        if i in chars:
            return False
        
        chars.append(i)
    
    return True
