func scoreOfString(s string) int {
    sum := 0
    for i, _ := range s {
        if i == len(s)-1 {
            break
        }
        sum = sum + int(math.Abs(float64(s[i]) - float64(s[i+1])))
    }
    return sum
}