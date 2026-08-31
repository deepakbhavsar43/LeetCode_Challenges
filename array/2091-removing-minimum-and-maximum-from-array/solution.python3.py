class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n =len(nums)
        if n <= 1:
            return n
        else:
            print(f"List: {nums}")
            min_value = min(nums)
            max_value = max(nums)
            min_index = nums.index(min_value)
            max_index = nums.index(max_value)
            
            print(f"Min Value: {min_value} at index {nums.index(min_value)} and Max Value: {max_value} at index {nums.index(max_value)}")
            
            i = min(min_index, max_index)
            j = max(min_index, max_index)

            front = j+1
            back = n-i
            both = (i+1) + (n-j)

            return min(front, back, both)
        
