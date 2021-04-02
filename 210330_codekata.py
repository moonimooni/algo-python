def reverse(number):
    number = str(number)

    if number[-1] == '0':
        number = number[:-1]

    if not number[0].isdigit():
        string = number[0]
        number = number[1:]
        return int(string + number[::-1])

    return int(number[::-1])

print(reverse(1440))