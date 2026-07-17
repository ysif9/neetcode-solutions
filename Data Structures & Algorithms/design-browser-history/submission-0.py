class ListNode:

    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(homepage) # head
        self.tail = self.head

    def visit(self, url: str) -> None:
        new = ListNode(url)
        self.tail.next = new
        new.prev = self.tail
        self.tail = new
        

    def back(self, steps: int) -> str:
        curr = self.tail
        for i in range(steps):
            curr = curr.prev if curr.prev else curr
            self.tail = curr
        return curr.val
        

    def forward(self, steps: int) -> str:
        curr = self.tail
        for i in range(steps):
            curr = curr.next if curr.next else curr
            self.tail = curr
        return curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

# homepage -> urls
# back or forward

# [] <->  [] <->  [] <->  []