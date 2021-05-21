# Linked list

+ [ Merge k Sorted Lists](#merge-k-sorted-lists)

##  Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/
```python
def min_idx(self, lists):
    idx = 0

    for i in range(len(lists)):
        if lists[i].val < lists[idx].val:
            idx = i
    return idx

def mergeKLists(self, lists):
    head = tail = ListNode(-1)

    lists = list(filter(lambda x: x is not None, lists))

    while len(lists) > 0:
        m_idx = self.min_idx(lists)

        tail.next = lists[m_idx]
        tail = tail.next
        lists[m_idx] = lists[m_idx].next

        if lists[m_idx] is None:
            del lists[m_idx]

    return head.next
```