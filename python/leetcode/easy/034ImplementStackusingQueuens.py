class Stack:
    def __init__(self):
        self.queue1 = []

    def push(self, x):
        self.queue1.append(x)

    def pop(self):
        if len(self.queue1) == 0:
            pass
        elif len(self.queue1) == 1:
            self.queue1 = []
        else:
            self.queue1 = self.queue1[0:len(self.queue1)-1]

    def top(self):
        if len(self.queue1) == 0 :
            return None
        else:
            return self.queue1[len(self.queue1)-1]

    def empty(self):
        if len(self.queue1) == 0 :
            return True
        else:
            return False
