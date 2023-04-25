# https://leetcode.com/problems/interval-list-intersections/description/

from typing import List


class Solution:
    # intersecting 한다면
    # intersecting 한 부분을 append하고
    # pointer가 더 뒤에 있는 놈의 앞 chunk로 이동
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        ret = list()

        first_list_chunk_pointer, second_list_chunk_pointer = 0, 0
        first_list_chunk_pointer_limit, second_list_chunk_pointer_limit = len(firstList), len(secondList)

        if first_list_chunk_pointer_limit <= 0 or second_list_chunk_pointer_limit <= 0:
            return ret

        while first_list_chunk_pointer < first_list_chunk_pointer_limit and second_list_chunk_pointer < second_list_chunk_pointer_limit:
            first_list_chunk, second_list_chunk = firstList[first_list_chunk_pointer], secondList[second_list_chunk_pointer]
            
            is_intersecting = max(first_list_chunk) >= min(second_list_chunk) and max(second_list_chunk) >= min(first_list_chunk)
            
            if is_intersecting:
                ret.append([max(first_list_chunk[0], second_list_chunk[0]), min(first_list_chunk[1], second_list_chunk[1])])

            if first_list_chunk[1] > second_list_chunk[1]:
                second_list_chunk_pointer += 1
            elif first_list_chunk[1] < second_list_chunk[1]:
                first_list_chunk_pointer += 1
            else:
                second_list_chunk_pointer += 1
                first_list_chunk_pointer += 1

        return ret

s = Solution()
print(s.intervalIntersection([[10,12],[18,19]], [[1,6],[8,11],[13,17],[19,20]]))
print(s.intervalIntersection([[1,3],[5,9]], []))
print(s.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))
