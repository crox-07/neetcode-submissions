class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = set()
        for i in nums:
            if i in numbers:
                return True
            else:
                numbers.add(i)
        return False