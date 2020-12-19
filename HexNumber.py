class Node:
    def init(self, value=None, next=None):
        self.value = value
        self.next = next


class HexNumber:
    def init(self, num):
        self.len = len(num)
        a = Node(num[-1])
        self.head = a
        for i in range(1, len(num)):
            a.next = Node(num[::-1][i])
            a = a.next

    def add(self, num):
        pass
        return 0

    def str(self):
        res = ""
        head = self.head
        for i in range(self.len):
            head.value = str(head.value)
            res = res + head.value
            head = head.next
        return res


def main(num1, num2):
    num1 = HexNumber(num1)
    num2 = HexNumber(num2)
    num3 = num1.add(num2)
    print(num3)


if name == 'main':
    print(HexNumber(''))