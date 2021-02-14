how_many_nums = int(input())
order_of_nums = list(int(input()) for i in range(how_many_nums))

def stack_1(nums_total, nums_sequence):
  stack, answer = [0], list()
  count = [i+1 for i in range(nums_total)]
  count_point = 0

  for j in nums_sequence:
    if j >= stack[-1]:
      if j > stack[-1]:
        for k in range(j - count_point):
          answer.append('+')
        stack += count[count_point:j]
        count_point = j
      answer.append('-')
      stack.pop()
    else:
      print('NO')
      exit(0)
  print('\n'.join(answer))

stack_1(how_many_nums, order_of_nums)