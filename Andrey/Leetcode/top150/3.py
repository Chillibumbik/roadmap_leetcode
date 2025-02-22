class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        lenght = len(nums)
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == nums[i-1]:
                del nums[i]
                lenght -= 1
        return lenght