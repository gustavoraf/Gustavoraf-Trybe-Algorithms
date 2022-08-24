def is_palindrome_iterative(word):
    if not word:
        return False
    half = len(word) // 2
    lasts = -1
    for index in range(half):
        if word[index] != word[lasts]:
            return False
        lasts -= 1
    return True
