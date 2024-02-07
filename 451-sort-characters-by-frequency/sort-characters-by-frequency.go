func SortMap(m map[rune]int) []rune {
    keys := make([]rune, 0, len(m))
    for key := range m {
        keys = append(keys, key)
    }
    sort.SliceStable(keys, func(i, j int) bool{
        return m[keys[i]] > m[keys[j]]
    })
    return keys
}
func frequencySort(s string) string {
    freq := map[rune]int{}
    result := ""
    for _, char := range s{
        freq[char] = freq[char] + 1 
    }
    sortedKeys := SortMap(freq)
    for _,key := range sortedKeys {
        for i := 0; i<freq[key]; i++ {
            result+=string(key)
        }
    }
    return result
}