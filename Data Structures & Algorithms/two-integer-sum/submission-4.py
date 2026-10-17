class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        items = {}
        if len(nums) == 0:
            return
        for i in range(len(nums)):
            num = nums[i]
            if num in items:
                elem = items[num]
                elem[0].append(i)
                items[num] = (elem[0], elem[1] + 1)
            else:
                items[num] = ([i], 1)
        print
        for k, v in items.items():
            diff = target - k
            if diff == k and v[1] > 1:
                print(v)
                r1 = v[0][0]
                r2 = v[0][1]
                if r1 < r2:
                    return [r1, r2]
                else:
                    return [r2, r1]
            if diff in items and v[0][0] != items[diff][0][0]:
                r1 = v[0][0]
                r2 = items[diff][0][0]
                if r1 < r2:
                    return [r1, r2]
                else:
                    return [r2, r1]
