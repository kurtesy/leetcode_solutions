func validPartition(nums []int) bool {
    dp1, dp2, dp3 := true, false, nums[0]==nums[1]
    
    for i := 2; i < len(nums); i++ {
        dp1, dp2, dp3 = dp2, dp3, nums[i-1]==nums[i] && (dp2 || (nums[i-2]==nums[i-1] && dp1)) || (nums[i-2]+1 == nums[i-1] && nums[i-1]+1 == nums[i] && dp1)
    }
    
    return dp3
}