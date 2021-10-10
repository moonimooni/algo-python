# https://programmers.co.kr/learn/courses/30/lessons/17681

def converter(n, length):
    result = format(n, 'b')
    while len(result) != length:
        result = '0' + result
    return result

def solution(n, arr1, arr2):
    answer = ['']*n
    for i in range(n):
        
        arr1_val = converter(arr1[i], n)
        arr2_val = converter(arr2[i], n)
        
        for j in range(n):
            if arr1_val[j] == '1' or arr2_val[j] == '1':
                answer[i] += '#'
            else:
                answer[i] += ' '
                
    return answer

#다른 사람 풀이

# def solution(n, arr1, arr2):
#     answer = []
#     for i,j in zip(arr1,arr2):
#         a12 = str(bin(i|j)[2:]) #아 대박
#         a12=a12.rjust(n,'0')
#         a12=a12.replace('1','#')
#         a12=a12.replace('0',' ')
#         answer.append(a12)
#     return answer

print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))