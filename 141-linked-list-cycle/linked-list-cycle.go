/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func contains(list []ListNode, node ListNode) bool {
    for _, curNode := range list {
        if curNode == node {
            return true
        }
    }
    return false
}

func hasCycle(head *ListNode) bool {
    track := []ListNode{}
    for head != nil {
        if contains(track, *head) {
            return true
        }
        track = append(track, *head)
        head = head.Next
    }
    return false
}