def format_duration(seconds):
    if seconds == 0:
        return "now"
    intervals = [('year', 365 * 24 * 60 * 60),('day', 24 * 60 * 60),('hour', 60 * 60),('minute', 60),('second', 1)]
    result = []
    for name, count in intervals:
        value = seconds // count
        if value:
            if value == 1:
                result.append(f"{value} {name}")
            else:
                result.append(f"{value} {name}s")
            seconds %= count
    if len(result) == 1:
        return result[0]
    else:
        return ', '.join(result[:-1]) + ' and ' + result[-1]
