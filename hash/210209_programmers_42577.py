# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    
    phone_book.sort(key=len)
    hash_dict = dict()
    hash_dict[hash(phone_book[0])] = phone_book[0]
    hashlen = len(phone_book[0])
    
    for phone_num in phone_book[1:]:
        if len(phone_num) == hashlen:
            hash_dict[hash(phone_num)] = phone_num
        elif len(phone_num) > hashlen:
            if hash(phone_num[:hashlen]) in hash_dict.keys():
                return False
    
    return True

# p = ['119', '97674223', '1195524421']
# p = ['123','456','789']
p = ['12','123','1235','567','88']

print(solution(p))