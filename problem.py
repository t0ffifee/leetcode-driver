from typing import List

class Solution:
  def solution(self, nums: List[int], target: int) -> List[int]:
    hashmap = {} # number, index

    for i, n in enumerate(nums):
      complement = target - n
      index = hashmap.get(complement, -1)
      if index >= 0:
        return [i, index]
      else:
        hashmap[n] = i

# parse testcases.txt

# run Solution.solution on them