class SinglyLinkedList(list):
    def __init__(self, *args, **kwd):
        super(SinglyLinkedList, self).__init__(*args, **kwd)

    def head(self):
        self.counter = 0
        return self[0]

    def tail(self):
        self.counter = len(self)
        return self[-1]

    def next(self):
        self.counter += 1
        return self[self.counter]

    def previous(self):
        self.counter -=1
        return self[self.counter]

newlist = SinglyLinkedList([1,2,3,4])
newlist.head()
# 1
newlist.tail()
# 4
newlist.head().next()
# 2
newlist.previous()
# 1