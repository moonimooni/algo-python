# https://programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    answer = ''

    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    words = s.split(' ')
    for word in words:
        for letter in word:
            isUpper = letter.isupper()
            idx = alphabets.find(letter.lower()) + n
            if idx >= len(alphabets):
                idx %= len(alphabets)
            if isUpper:
                answer += alphabets[idx].upper()
            else:
                answer += alphabets[idx]

        answer += ' '
    return answer[:-1]

print(solution('A xy z', 2))