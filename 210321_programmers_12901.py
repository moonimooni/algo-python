def solution(a, b):
    answer = ''
    of31,of30 = [1,3,5,7,8,10,12], [4,6,9,11]
    days = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    m_cnt, d_cnt = 1, 5
    
    if a == 1:
        d_cnt += (b-1)
        answer += days[d_cnt % 7]
        return answer
    while m_cnt != a:
        if m_cnt in of31:
            d_cnt += 31
        elif m_cnt in of30:
            d_cnt += 30
        else:
            d_cnt += 29
        m_cnt += 1
    d_cnt += (b-1)
    answer += days[d_cnt % 7]
        
    return answer

print(solution(4, 20))