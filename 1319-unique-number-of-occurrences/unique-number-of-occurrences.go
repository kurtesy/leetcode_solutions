func uniqueOccurrences(arr []int) bool {
    frequency := map[int]int{}
    for _, num := range arr {
        _, found := frequency[num]
        if found {
            frequency[num]+=1
        } else {
            frequency[num]=1
        }
    }
    done := []int{}
    for _, count := range frequency {
        if (slices.Contains(done, count)) {
            return false
        } else {
            done = append(done, count)
        }
    }
    return true
}