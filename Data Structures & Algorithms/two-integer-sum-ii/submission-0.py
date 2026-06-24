class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)):
            t = target - numbers[i]
            f, b = 0, len(numbers)-1 
            while f <= b:
                mid = (f + b) //2
                if numbers[mid] == t:
                    return list((i + 1, mid + 1))
                if numbers[mid] < t:
                    f = mid + 1  
                else:      
                    b = mid - 1
                 
            
