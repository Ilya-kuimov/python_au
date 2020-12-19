class MyLinkedList:
    class ListNode:

        def init(self, val: int, prev=None, nxt=None):
            self.prev, self.next = prev, nxt
            self.value = val

    def init(self):

        self.head, self.tail = self.ListNode(0), self.ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:

        node, pos = self.head.next, 0

        while node and pos < index:
            node, pos = node.next, pos + 1

        return node.value if node and node != self.tail else -1

    def addAtHead(self, val: int) -> None:

        new_node = self.ListNode(val, self.head, self.head.next)
        self.head.next.prev, self.head.next = new_node, new_node

    def addAtTail(self, val: int) -> None:

        new_node = self.ListNode(val, self.tail.prev, self.tail)
        self.tail.prev.next, self.tail.prev = new_node, new_node

    def addAtIndex(self, index: int, val: int) -> None:

        node, cur = self.head.next, 0

        while node and cur < index:
            if not node: return
            node = node.next
            cur += 1

        if not node: return

        new_node = self.ListNode(val, node.prev, node)
        node.prev.next, node.prev = new_node, new_node

    def deleteAtIndex(self, index: int) -> None:

        node, cur = self.head.next, 0

        while node and cur < index:
            if not node: return
            node = node.next
            cur += 1

        if not node or node == self.tail: return

        node.prev.next, node.next.prev = node.next, node.prev