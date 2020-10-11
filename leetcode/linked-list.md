+ [ Reorder List](#Reorder-List)
+ [ Middle of the Linked List](#Middle-of-the-Linked-List)
+ [ Merge Two Sorted Lists](#Merge-Two-Sorted-Lists)
+ [ Linked List Cycle](#Linked-List-Cycle)

##  Reorder List
https://leetcode.com/problems/reorder-list/
```python
class Solution:
    def reorderList(self, head):
        if not (head or head.next):
            return
        result = []
        MidIndex = head
        LastIndex = MidIndex.next
        while (LastIndex and LastIndex.next):
            MidIndex = MidIndex.next
            LastIndex = LastIndex.next.next
        Current_element = MidIndex.next
        MidIndex.next = None
        while (Current_element):
            result.append(Current_element)
            Current_element = Current_element.next
        Current_element = head
        while (len(result) > 0):
            result[-1].next = Current_element.next
            Current_element.next = result.pop()
            Current_element = Current_element.next.next
```
##  Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/
```python
class Solution:
    def middleNode(self, head):
        count,newhead = 0, 0
        current_element, middle_element = head, head
        while current_element:
            current_element = current_element.next
            count += 1
        if count % 2 != 0:
            newhead = int((count + 1) / 2)
        else:
            newhead = int((count / 2) + 1)
        for i in range(newhead - 1):
            middle_element = middle_element.next
```
##  Merge Two Sorted Lists
https://leetcode.com/problems/merge-intervals/
```python
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2
```
##  Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/
```python
class Solution:
    def hasCycle(self, head):
        visited_nodes=set()
        while head:
            if head in visited_nodes:
                return True
            visited_nodes.add(head)
            head=head.next
        return False
```

