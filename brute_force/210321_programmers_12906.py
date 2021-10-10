# def solution(arr):
#     answer = []
#     if len(arr) == 1:
#         return arr
    
#     for i in range(len(arr)-1):
#         if arr[i] == arr[i+1]:
#             arr[i] = False
    
#     for el in arr:
#         if type(el) == int:
#             answer.append(el)
    
#     return answer

# print(solution([1,1,3,3,0,1,1]))

def solution(arr):
    answer = []
    for el in arr:
        if answer[-1:] == [el]: 
            continue
        answer.append(el)
    return answer

print(solution([1,1,3,3,0,1,1]))