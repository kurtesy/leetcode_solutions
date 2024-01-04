func minOperations(nums []int) int {
    freq := map[int]int{}
    for _, n := range nums {
        _, found := freq[n]
        if (!found) {
            freq[n]=1
        } else {
            freq[n]=freq[n]+1
        }
    }
    result := 0
    for _, cnt := range freq {
        fmt.Println(cnt)
        if (cnt == 1) {
            return -1
        }
        result += cnt/3
        if (cnt%3!=0) {
            result += 1
        }
    }
    return result
}