def solution(a, b):
    answer = ''
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    
    cnt = sum(months[:a-1]) + (b-1) + 5
    answer += days[cnt%7]
    return answer
    
    # m_cnt, d_cnt = 1, 5
    # while m_cnt != a:
    #     if m_cnt in of31:
    #         d_cnt += 31
    #     elif m_cnt in of30:
    #         d_cnt += 30
    #     else:
    #         d_cnt += 29
    #     m_cnt += 1
    # d_cnt += (b-1)
    # answer += days[d_cnt % 7]
        
    # return answer

print(solution(5, 24))