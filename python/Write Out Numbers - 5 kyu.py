def number2words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    def words(num):
        if num < 10:
            return ones[num]
        elif num < 20:
            return teens[num - 10]
        elif num < 100:
            return tens[num // 10] + ("-" + ones[num % 10] if num % 10 != 0 else "")
        elif num < 1000:
            return ones[num // 100] + " hundred" + (" " + words(num % 100) if num % 100 != 0 else "")
    
    if n == 0:
        return "zero"
    elif n < 1000:
        return words(n)
    else:
        thousands, remainder = divmod(n, 1000)
        return words(thousands) + " thousand" + (" " + words(remainder) if remainder != 0 else "")
