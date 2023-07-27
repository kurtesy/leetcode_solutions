class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        slow = 0
        for fast in range(1,len(numbers)):
            if numbers[fast] + numbers[slow] == target:
                return [slow+1, fast+1]
            elif numbers[fast] + numbers[slow] < target:
                slow+=1
        