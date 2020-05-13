class Solution:
    def majorityElement(self, nums = []) -> int:
        tempset = set(nums)
        max_count = 0
        max_cmd = ''
        if len(nums) == 0:
            return len(nums)
        while len(tempset) > 0:
            cmd = tempset.pop()
            temp = list(filter(lambda a: a != cmd, nums))
            if len(nums) - len(temp) > max_count:
                max_count = len(nums) - len(temp)
                max_cmd = cmd

        return max_cmd