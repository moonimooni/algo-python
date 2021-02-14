import hashlib

participant = ['leo', 'kiki', 'eden']
completion = ['eden', 'kiki']
# participant = ['marina', 'josipa', 'nikola', 'vinko', 'filipa']
# completion = ['josipa', 'filipa', 'marina', 'nikola']
# participant = ['mislav', 'stanko', 'mislav', 'ana']
# completion = ['stanko', 'ana', 'mislav']

def solution(participant, completion):
    hash_dict = dict()

    for name in participant:
        hash_adr = hash(name)
        if hash_adr in hash_dict.keys():
            hash_dict[hash_adr].append(name)
        else:
            hash_dict[hash_adr] = [name]
    
    for cpl in completion:
        hash_adr = hash(cpl)
        hash_dict[hash_adr].pop()
        if hash_dict[hash_adr] == []:
            del hash_dict[hash_adr]

    answer = list(hash_dict.values())[0][0]
    return answer

print(solution(participant, completion))