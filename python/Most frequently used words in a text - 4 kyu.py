from collections import Counter
def top_3_words(text):
    text = text.lower()
    words = []
    current = []
    for ch in text:
        if ('a' <= ch <= 'z') or ch == "'":
            current.append(ch)
        else:
            if current:
                word = ''.join(current)
                if any('a' <= c <= 'z' for c in word):
                    words.append(word)
                current = []
    if current:
        word = ''.join(current)
        if any('a' <= c <= 'z' for c in word):
            words.append(word)
    counts = Counter(words)
    return [word for word, _ in counts.most_common(3)]
