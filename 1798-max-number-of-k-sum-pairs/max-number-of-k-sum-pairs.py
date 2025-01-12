from collections import defaultdict
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count: int = 0
        occurances: defaultdict = defaultdict(int)

        for num in nums:
            target: int = k - num
            if occurances[target] > 0:
                count = count + 1
                occurances[target] -= 1
            else:
                occurances[num] += 1
        return count
