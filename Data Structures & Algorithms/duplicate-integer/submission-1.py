class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # solution 2

        return len(set(nums)) < len(nums)

        # solution 1
        # s = sorted(nums)
        # for i in range(len(s)-1):
        #     a = s[i]
        #     # print("this is a ",a)
        #     if a != s[i+1]:
        #         continue
        #     else:
        #         return True
        # return False
