class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.item = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.item.append(x)

    # @return nothing
    def pop(self):
        self.item.pop(0)

    # @return an integer
    def peek(self):
        return self.item[0]

    # @return an boolean
    def empty(self):
        return len(self.item)==0

if __name__ == "__main__":
    a = Queue()
    print a.peek()
    a.push(1)
    a.push(2)
    a.push(3)
    a.push(4)
    print a.peek()
    a.pop()
    a.pop()
    print a.peek()
    print a.empty()
