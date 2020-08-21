'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    print(f"word being tested: {word}")
    if len(word) == 1:  # base case, ends recursion
        return 0
    elif len(word) == 0:
        return 0  # just in case

    # TBC
    # will recurse through the word jumping 1 letter at a time, 2 if its a th

    if word[0] == "t":  # is first letter t?
        if word[1] == "h":  # if yes, checks for an h
            # if yes, returns 1 found and recurses onward
            return 1 + count_th(word[1:])
        else:  # not an h, recurses onward
            return count_th(word[1:])
    else:  # not a t, continues
        return count_th(word[1:])
