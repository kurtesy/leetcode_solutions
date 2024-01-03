import (
    "fmt"
    "math"
    "reflect"
)

func isPowerOfFour(n int) bool {
    if (n <= 0) {
        return false
    }
    log_val := math.Log(float64(n))/math.Log(4)
    if (log_val == math.Trunc(log_val)) {
        return true
    }
    fmt.Println(reflect.TypeOf(log_val))
    return false
}