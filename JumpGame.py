class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n in [0,1]:
            return True
        dp = [0 for i in range(n)]
        dp[0] = nums[0]
        for i in range(1,n):
            #index that you can jump to atmost
            if dp[i-1]<i:
                return False
            dp[i] = max(dp[i-1], i+nums[i])
            if dp[i]>=n:
                dp[i] = n-1
        print (dp)
        return (dp[n-1]==n-1)
