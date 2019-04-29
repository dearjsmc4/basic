'''
class Stack:
    def __init__(self):
        self.container=list()

    # 스택이 비어있으면 True, 아니면 False
    def empty(self):
        if not self.container:
            return True
        return False

    # 스택의 맨 위에 데이터 쌓기
    def push(self, data):
        self.container.append(data)
    
    # 래퍼 함수(wrapper function)
    # 스택의 맨 위 데이터를 삭제하며 반환
    def pop(self):
        return self.container.pop()
    
    # 스택의 맨 위 데이터를 반환
    def peek(self):
        return self.container[-1]

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(52)

while not stack.empty():
    print(stack.peek())

'''


class Queue:
    def __init__(self):
        self.container=list()

    def empty(self):
        if not self.container:
            return True
        return False

    def enqueue(self, data):
        self.container.append(data)
    
    def dequeue(self):
        return self.container.pop(0)
    
    def peek(self):
        return self.container[0]



q = Queue()

for i in range(1,6):
    q.enqueue(i)

while not q.empty():
    print(q.dequeue())


