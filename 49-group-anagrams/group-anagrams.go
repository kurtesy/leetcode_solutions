func SortString(w string) string {
    s := strings.Split(w, "")
    sort.Strings(s)
    return strings.Join(s, "")
}
func groupAnagrams(strs []string) [][]string {
    result := [][]string{}
    anaMap := map[string][]int{}
    for index, s := range strs {
        key := SortString(s)
        anaMap[key] = append(anaMap[key], index)
    }
    for _, vals := range anaMap {
        temp := []string{}
        for _,index := range vals {
            temp = append(temp, strs[index])
        }
        result = append(result, temp)
    }
    return result
}