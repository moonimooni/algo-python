# https://programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    answer = ''
    special = ['-', '_', '.']
    
    #1단계
    new_id = new_id.lower() 
    #2단계
    new_id = ''.join([x for x in new_id if x.isalnum() or x in special])
    #3단계
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    #4단계
    if new_id[0] == '.': 
        new_id = new_id[1:]
    elif new_id[-1] == '.': 
        new_id = new_id[:-1]
    #5단계
    if not new_id:
        new_id += 'a'
    #6단계
    if len(new_id) >= 16: 
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    
    #7단계
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += new_id[-1]
    answer += new_id
    return answer