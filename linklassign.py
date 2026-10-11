class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def solve(self, head, value, pos, delete_value):
        # Insert at position
        new = ListNode(value)
        if pos == 0:
            new.next = head
            head = new
        else:
            t = head
            for _ in range(pos - 1):
                if t is None:
                    break
                t = t.next
            if t:
                new.next = t.next
                t.next = new

        # Find middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow.val if slow else None

        # Delete node by value
        if head and head.val == delete_value:
            head = head.next
        else:
            t = head
            while t and t.next:
                if t.next.val == delete_value:
                    t.next = t.next.next
                    break
                t = t.next

        # Reverse list
        prev = None
        t = head
        while t:
            nxt = t.next
            t.next = prev
            prev = t
            t = nxt
        head = prev

        # Consecutive sums
        sums = []
        t = head
        while t and t.next:
            sums.append(t.val + t.next.val)
            t = t.next

        return head, middle, sums