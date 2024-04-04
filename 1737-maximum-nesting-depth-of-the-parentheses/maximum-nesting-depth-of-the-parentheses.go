func maxDepth(s string) int {
    maxLen := 0
    depth := 0
    for _,char := range s {
        if string(char) == "(" {
            depth++
            if depth > maxLen {maxLen=depth}
        } else if string(char) == ")" {
            depth--
        }
    }
    return maxLen
}