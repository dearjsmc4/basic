
# 스택 두 개를 이용해 큐를 구현하기

class Stack:
    def __init__(self):
        self.container=list()

    def empty(self):
        if not self.container:
            return True
        return False

    def push(self, data):
        self.container.append(data)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]


class Queue:
    def __init__(self):
        self.first=Stack()
        self.second=Stack()
    
    def empty(self):
        if self.first.empty() and self.second.empty():
            return True
        return False
    
    def enqueue(self, data):
        self.first.push(data)

    def dequeue(self):
        if self.empty():
            return None
        
        # first 에서 second 로 옮기는 시점
        # second 가 비었을 때.
        if self.second.empty():
            while not self.first.empty():
                self.second.push(self.first.pop())
        return self.second.pop()

    def peek(self):
        pass

q = Queue()
'''
for i in range(1,6):
    q.enqueue(i)

while not q.empty():
    print(q.dequeue())

'''
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())

q.enqueue(4)
q.enqueue(5)

while not q.empty():
    print(q.dequeue())
