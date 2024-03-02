func sortedSquares(nums []int) []int {
    result := []int{}
    for _, n := range nums {
        result = append(result, n*n)
    }
    slices.Sort(result)
    return result
}