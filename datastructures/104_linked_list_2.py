class Node:
    def __init__(self, data, next_=None):
        self.data = data
        self.next_ = next_


class LinkedList:
    def __init__(self, head):
        self.head = head

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next_
        return count

    def find(self, index):
        if self.head is None:
            return Node(None)
        else:
            count = 0
            current = self.head
            while current:
                if count == index:
                    return current
                count += 1
                current = current.next_
            return Node(None)

    def insert(self, index, node):
        if index < 0 or index > self.size() - 1:
            return "Index out of range"
        elif index == 0:
            node.next_ = self.head
            self.head = node
            return "Node created"
        else:
            before = self.find(index - 1)
            after = self.find(index)
            before.next_ = node
            node.next_ = after
            return "Node created"

    def add(self, node):
        size = self.size()
        if size == 0:
            self.head = node
        else:
            last = self.find(size - 1)
            last.next_ = node

    def __str__(self):
        current = self.head
        nodes = []
        index = 0
        while current:
            nodes.append(f"index: {index} data: {current.data}")
            index += 1
            current = current.next_
        nodes = " ,".join(nodes)
        return f"Linked list: {nodes}"


node3 = Node(30)
node2 = Node(20)
node1 = Node(10)
node0 = Node(0)

l = LinkedList(node0)
l.add(node1)
l.add(node3)

print(f"Size: {l.size()}")
print(f"Node: {l.find(3).data}")
print(l)