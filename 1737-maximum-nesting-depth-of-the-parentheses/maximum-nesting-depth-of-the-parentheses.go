func maxDepth(s string) int {
    maxLen := 0
    depth := 0
    for _,char := range s {
        if string(char) == "(" {
            depth++
            maxLen = max(maxLen, depth)
        } else if string(char) == ")" {
            depth--
        }
    }
    return maxLen
}