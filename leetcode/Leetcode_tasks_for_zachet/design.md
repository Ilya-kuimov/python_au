# Design

+ [ Min Stack](#min-stack)
+ [ Implement Queue using Stacks](#implement-queue-using-stacks)
+ [ Implement Stack using Queues](#implement-stack-using-queues)

##  Min Stack
https://leetcode.com/problems/min-stack/
```python
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mini = sys.maxint
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        
        if x <= self.mini:
            self.stack.append(self.mini)
            self.mini = x
        
        self.stack.append(x)
        
    def pop(self):
        """
        :rtype: void
        """
        res = self.stack.pop()
        if res == self.mini:
            self.mini = self.stack.pop()
            
        
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        
    def getMin(self):
        """
        :rtype: int
        """
        return self.mini
```
## Implement Queue using Stacks 
https://leetcode.com/problems/implement-queue-using-stacks/
```python
class MyQueue:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.inStack, self.outStack = [], []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.inStack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.move()
        return self.outStack.pop()

    def peek(self):
        """
        :rtype: int
        """
        self.move()
        return self.outStack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return (not self.inStack) and (not self.outStack)

    def move(self):
        """
        :rtype nothing
        """
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
```
## Implement Stack using Queues
https://leetcode.com/problems/implement-stack-using-queues/
```python
class MyStack {
public:
    MyStack() {}
    void push(int x) {
        q2.push(x);
        while (q2.size() > 1) {
            q1.push(q2.front()); q2.pop();
        }
    }
    int pop() {
        int x = top(); q2.pop();
        return x;
    }
    int top() {
        if (q2.empty()) {
            for (int i = 0; i < (int)q1.size() - 1; ++i) {
                q1.push(q1.front()); q1.pop();
            }
            q2.push(q1.front()); q1.pop();
        }
        return q2.front();
    }
    bool empty() {
        return q1.empty() && q2.empty();
    }
private:
    queue<int> q1, q2;
};
```
