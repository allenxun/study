class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        if len(self.minStack) == 0 or self.minStack[-1][0] > x:
            self.minStack.append((x,1))
        elif x == self.minStack[-1][0]:
            self.minStack[-1] = (x, self.minStack[-1][1] + 1)

    def pop(self):
        """
        :rtype: nothing
        """
        pop = self.stack.pop()
        if pop == self.minStack[-1][0]:
            if self.minStack[-1][1] > 1:
                self.minStack[-1] = (self.minStack[-1][0], self.minStack[-1][1] - 1)
            else:
                self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1][0]
        
