class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = []
        i = 0
        nums.sort()
        for i in range(len(nums)):
            left = i +1 
            right = len(nums) -1 
            while left < right: 
                triplet = [nums[i], nums[left], nums[right]]
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    if triplet not in s:
                        s.append(triplet)
                    right -= 1 
                    left += 1
                elif total < 0:             
                    left += 1 
                else: 
                    right -= 1 
        
        return s



    