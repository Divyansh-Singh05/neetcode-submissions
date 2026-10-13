class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = 0
        max_list = []
        max_num = float("-inf")

        while r < len(nums):
            max_num = max(nums[r], max_num)

            if r - l + 1 == k:
                max_list.append(max_num)

                if nums[l] == max_num:
                    if l + 1 <= r:
                        max_num = max(nums[l + 1:r + 1])
                    else:
                        max_num = float("-inf")

                l += 1

            r += 1

        return max_list