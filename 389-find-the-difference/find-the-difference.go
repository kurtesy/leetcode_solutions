func findTheDifference(s string, t string) byte {
    arr := make([]int, 26)

    for i := 0; i < len(s); i++ {
        arr[s[i] - 'a'] -= 1
    }

    for i := 0; i < len(t); i++ {
        arr[t[i] - 'a'] += 1
    }

    for i, x := range arr {
        if x == 1 {
            return byte(i + 'a')
        }
    }

    return byte(0)
}