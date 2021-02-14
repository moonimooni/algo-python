# https://www.acmicpc.net/problem/2839

total_kg = int(input())
smaller, larger = 3, 5

def deliver(kg_left, count, pkg_size, max_quotient):
  if max_quotient <= 0:
    if pkg_size == smaller:
      return -1
    else:
      pkg_size = smaller
      max_quotient = kg_left // pkg_size

  while pkg_size >= 3:
    max_kg = pkg_size * max_quotient
    if kg_left - max_kg == 0:
      count += max_quotient
      return count

    elif (kg_left - max_kg) % smaller != 0:
      max_quotient -= 1
      return deliver(kg_left, count, pkg_size, max_quotient)
    elif (kg_left - max_kg) % smaller == 0:
      count += max_quotient
      pkg_size = smaller
      kg_left -= max_kg
      return deliver(kg_left, count, pkg_size, kg_left // pkg_size)

  return -1

print(deliver(total_kg, 0, larger, total_kg // larger))


## 다른 사람 풀이

# import sys
# N = int(sys.stdin.readline())
# a = 0
# while N > 0:
#     if N >= 15 or N == 5 or N ==10:
#         N -= 5
#     elif N > 0:
#         N -= 3
#     a+=1
#     if N < 0:
#         break

# if N != 0:
#     print(-1)
# else:
#     print(a)