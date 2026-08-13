class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)

        for i in range(len(nums)):
            prefix[i] = nums[i] * prefix[i-1] if i > 0 else nums[i]

        for i in range(len(nums)-1, -1, -1):
            suffix[i] = nums[i] * suffix[i+1] if i < len(nums) -1 else nums[i]

        print("pre", prefix)
        print("suf", suffix)

        res = [0] * len(nums)

        for i in range(len(nums)):
            pre = prefix[i-1] if i > 0 else 1
            suf = suffix[i+1] if i < len(nums) - 1 else 1
            res[i] = pre*suf

        return res