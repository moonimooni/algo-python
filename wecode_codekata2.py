import re

def reverse(number):
    # 여기에 코드를 작성해주세요.
    stringified = str(number)
    mark = ''

    if not stringified[0].isalnum():
        mark += stringified[0]
        stringified = stringified[1:]

    if stringified[-1] == '0' and len(stringified) > 1 :
        stringified = stringified[:-1]
    
    return int(mark + stringified[::-1])

print(reverse(0))