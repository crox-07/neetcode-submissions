class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_count = {}
        for i in range(len(nums)):
            if nums[i] in num_count:
                num_count[nums[i]][0] +=1
                num_count[nums[i]][1].append(i)
            else:
                num_count[nums[i]] = [1, [i]]
        for key, val in num_count.items():
            diff = target - key
            if diff in num_count:
                r1 = val[1][0]
                r2 = num_count[diff][1][0]
                if diff == key and val[0] > 1:
                    return val[1]
                elif r1 < r2:
                    return [r1, r2]
                elif r2 > r1:
                    return [r2, r1] 
