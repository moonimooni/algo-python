import re

string = 'Anna sees Bob'

def isPalindrome(string: str) -> bool:
    string = re.sub('\W', '', string)
    return string == string[::-1]

print(isPalindrome(string))