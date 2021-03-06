# Linked List

+ [ Reorder List](#Reorder-List)
+ [ Middle of the Linked List](#Middle-of-the-Linked-List)
+ [ Merge Two Sorted Lists](#Merge-Two-Sorted-Lists)
+ [ Linked List Cycle](#Linked-List-Cycle)
+ [ Palindrome Linked List](#Palindrome-Linked-List)
+ [ Remove Nth Node From End of List](#Remove-Nth-Node-From-End-of-List)
+ [ Reverse Linked List](#Reverse-Linked-List)
+ [ Linked List Cycle II](#Linked-List-Cycle-II)
+ [ Intersection of Two Linked Lists](#intersection-of-two-linked-lists)
+ [ Sort List](#sort-list)

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
##  Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/
```python
class Solution:
    def isPalindrome(self, head):
        if not head:
            return True

        def reverseList(head):
            if not (head and head.next):
                return head
            previous_element = None
            current_element = head
            while current_element:
                next = current_element.next
                current_element.next = previous_element
                previous_element = current_element
                current_element = next
            head = previous_element
            return head
        memory_head = head
        count, midPointer = 0, 0
        newhead = head
        while (head):
            if (midPointer != count // 2):
                newhead = newhead.next
                midPointer = count // 2
            count += 1
            head = head.next
        secondHalf = reverseList(newhead.next)
        check = True
        while (memory_head and secondHalf):
            if (memory_head.val != secondHalf.val):
                check = False
            memory_head = memory_head.next
            secondHalf = secondHalf.next
        return check
```
##  Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
```python
class Solution:
    def removeNthFromEnd(self, head, n):
        result = head
        length = 0
        count = 1
        while result:
            result = result.next
            length += 1
        result = head
        number_to_delete = length - n
        if number_to_delete == 0:
            head = head.next
        else:
            while count < number_to_delete:
                result = result.next
                count += 1
            result.next = result.next.next
        return head
```
##  Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/
```python
class Solution:
    def reverseList(self, head):
        if not (head and head.next):
            return head
        previous_element = None
        current_element = head
        while current_element:
            next = current_element.next
            current_element.next = previous_element
            previous_element = current_element
            current_element = next
        head = previous_element
        return head
```
##  Linked List Cycle II
https://leetcode.com/problems/linked-list-cycle-ii/
```python
class Solution:
    def detectCycle(self, head):
        visited_nodes=set()
        while head:
            if head in visited_nodes:
                return head
            visited_nodes.add(head)
            head=head.next
```
##  Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/
```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1 = headА
        p2 = headB
        while p1 != p2
            if p1:
                p1 = pl.next
            else:
                p1 = heads
            if pa:
                p2 = p2.next
            else:
                p2 = headA
        return p1
```
##  Sort List
https://leetcode.com/problems/sort-list/
```python
class Solution {
public:
    ListNode* sortList(ListNode* head) {
        const auto len = lenOf(head);
        
        if (len > 1) {
            head = mergeSort(head, len);
        }
        
        return head;
    }
    
    int lenOf(const ListNode* head) {
        int len {};
        
        for (auto cursor = head; cursor; cursor = cursor->next) {
            ++len;
        }
        
        return len;
    }
    
    ListNode* mergeSort(ListNode* list, const int len) {
        if (len <= 1) {
            return list;
        }
        
        auto list1 = list;
        auto list1Tail = advance(list, len / 2 - 1);
        auto list2 = list1Tail->next;
        
        list1Tail->next = nullptr;
        
        // proof: len / 2 < len when len > 1
        // proof: len - len / 2 < len when len > 1
        list1 = mergeSort(list1, len / 2);
        list2 = mergeSort(list2, len - len / 2);
        
        return merge(list1, list2);
    }
    
    ListNode* advance(ListNode* list, const int len) {
        for (int i = 0; i < len; ++i) {
            // [head, head + i] are skippted
            list = list->next;
        }
        
        // [head, head + len] are skipped
        
        return list;
    }
    
    ListNode* merge(ListNode* list1, ListNode* list2) {
        ListNode dummyHead { 0 };
        
        auto mergedTail = &dummyHead;
        
        // inv: [head, mergedTail] sorted
        // inv: [list1, ...) need merge
        // inv: [list2, ...) need merge
        while (list1 && list2) {
            const auto v1 = list1->val;
            const auto v2 = list2->val;
            
            if (v1 < v2) {
                mergedTail->next = list1;
                
                list1 = list1->next;
            } else {
                mergedTail->next = list2;
                
                list2 = list2->next;
            }
            
            mergedTail = mergedTail->next;
            // advance
            // mergedTail has been advanced
            // either list1 or list2 has been advanced
        }
        
        if (list1) {
            mergedTail->next = list1;
        } else {
            mergedTail->next = list2;
        }
        
        return dummyHead.next;
    }
};
```