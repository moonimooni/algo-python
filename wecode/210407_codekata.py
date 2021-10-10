def is_valid(string):
    half = len(string) // 2 - 1

    couple = {
        '(' : ')',
        '{' : '}',
        '[' : ']'
    }

    for i in range(half):
        if couple[string[i]] not in string:
            return False
        
        _i = string.index(couple[string[i]])

        if (_i - i) % 2:
            return True
    return False
