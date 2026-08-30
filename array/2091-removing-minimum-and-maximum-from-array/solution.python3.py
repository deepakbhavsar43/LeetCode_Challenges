class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        else:
            dup_nums = nums.copy()
            dup_nums.sort()
            # print(f"List: {nums}")
            total_nums=len(nums)
            min = dup_nums[0]
            max = dup_nums[total_nums-1]
            min_index = nums.index(min)
            max_index = nums.index(max)
            # print(f"til min front: {nums[:min_index+1]}")
            # print(f"til min reverse: {nums[:min_index-1:-1]}")
            
            min_deletions_front = len(nums[:min_index+1])
            min_deletions_reverse = len(nums[:min_index-1:-1])
            max_deletions_front = len(nums[:max_index+1])
            max_deletions_reverse = len(nums[:max_index-1:-1])

            max_array = [max_deletions_front, max_deletions_reverse]
            min_array = [min_deletions_front, min_deletions_reverse]
            # print(f"min_array:\n{min_array}")
            # print(f"max_array:\n{max_array}")
            if min_array[0] > min_array[1] and max_array[0] > max_array[1]:
                if min_array[1] > max_array[1]:
                    return max_array[1]
                else:
                    return min_array[1]
            elif min_array[0] < min_array[1] and max_array[0] < max_array[1]:
                if min_array[0] > max_array[0]:
                    return min_array[0]
                else:
                    return max_array[0]
            elif min_array[0] > min_array[1] and max_array[0] < max_array[1]:
                return min_array[1] + max_array[0]
            elif min_array[0] < min_array[1] and max_array[0] > max_array[1]:
                return min_array[0] + max_array[1]
        