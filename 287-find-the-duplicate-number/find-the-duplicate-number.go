func findDuplicate(nums []int) int {
    d := map[int]int{}
    for _,i := range nums {
        val := d[i]
        if val == 0 {
            d[i]++
        } else {
            return i
        }
    }
    return -1
}