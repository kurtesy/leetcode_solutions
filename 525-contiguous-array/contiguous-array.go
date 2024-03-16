func findMaxLength(nums []int) int {
    maxLen := 0
    cnt0 := 0
    cnt1 := 0
    dMap := map[int]int{0: -1}
    for idx, num := range nums {
        if num == 0 {
            cnt0++
        } else {
            cnt1++
        }
        diff := cnt0-cnt1
        val, found := dMap[diff]
        if found {
            maxLen = max(maxLen, idx-val)
        } else {
            dMap[diff] = idx
        }
        fmt.Println(val, maxLen, idx)
    }
    return maxLen
}