class Node:

    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None


    def isEmpty(self) -> bool:
        if self.head == None:
            return True
        return False
        

    def append(self, value: int) -> None:
        new = Node(value)
        if self.tail == None:
            self.head = new
            self.tail = self.head
        else:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new
        

    def appendleft(self, value: int) -> None:
        new = Node(value)
        if self.tail == None:
            self.head = new
            self.tail = self.head
        else:
            self.head.prev = new
            new.next = self.head
            self.head = new
        

    def pop(self) -> int:
        if self.head == None:
            return -1
        if self.head == self.tail:
            t = self.head
            self.head = None
            self.tail = None
            return t.val
        else:
            t = self.tail
            self.tail = self.tail.prev
            return t.val

        

    def popleft(self) -> int:
        if self.head == None:
            return -1
        if self.head == self.tail:
            t = self.head
            self.head = None
            self.tail = None
            return t.val
        else:
            t = self.head
            self.head = self.head.next
            return t.val