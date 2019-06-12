import math

scores = [3, 5, 2, 9, 12, 5, 23, 23]

def minimax(depth, idx, max_chance, scores, total_depth):
  # base case: depth == total_depth
  if depth == total_depth:
    return scores[idx]

  if max_chance:
    return max(minimax(depth + 1, idx * 2, False, scores, total_depth), minimax(depth + 1, idx * 2 + 1, False, scores, total_depth))
  else:
    return min(minimax(depth + 1, idx * 2, True, scores, total_depth), minimax(depth + 1, idx * 2 + 1, True, scores, total_depth))

total_depth = math.log2(len(scores))
print(minimax(0, 0, True, scores, total_depth))

