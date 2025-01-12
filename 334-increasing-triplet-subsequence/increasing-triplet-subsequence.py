class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first_max: int = (2**31) -1
        second_max: int = (2**31) - 1

        for num in nums: 
            if num <= first_max:
                first_max = num
            elif num <= second_max:
                second_max = num
            else:
                return True
        return False
        