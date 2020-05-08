class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        queue = []
        global queue

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        queue.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return queue.pop(0)

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        x=queue.pop(0)
        queue.insert(0,x)
        return x

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(queue)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()