# https://www.acmicpc.net/problem/2798

n, m = map(int, input().split())
nums_array = list(map(int, input().split()))

def blackjack(dealers_num, cards_array):
  answer = 0
  cards_array.sort(reverse=True)
  for i in range(len(cards_array)):
    for j in range(i+1, len(cards_array)):
      card1, card2 = cards_array[i], cards_array[j]
      if card1 + card2 < dealers_num:
        for k in range(j+1, len(cards_array)):
          card3 = cards_array[k]
          sum_of_cards = card1 + card2 + card3
          if sum_of_cards < answer:
            break
          if sum_of_cards <= dealers_num:
            answer = max(answer, sum_of_cards)
  return answer

print(blackjack(m, nums_array))