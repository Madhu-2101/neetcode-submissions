class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             result = [i, j]
        #             return result


        hashmap = {}
        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                result = [hashmap[target - nums[i]], i]
                return result
            else:
                hashmap[nums[i]] = i





        