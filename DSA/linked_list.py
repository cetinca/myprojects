from platform import node


class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

    def __str__(self):
        return f"< {self.data} >"

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        s = 0
        while current:
            s += 1
            current = current.next
        return s
    
    def add(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
    
    def search(self, key):
        current = self.head

        while current:
            if current.data == key:
                return current
            current = current.next
        return f"{key} not found!"
    
    def insert(self, data, index):
        if index == 0:
            self.add(data)
        
        if index > 0:
            node = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = current.next
                position -= 1
            
            previous = current
            next = current.next
            print(previous, next)

            previous.next = node
            node.next = next
    
    def remove(self, key):
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current == self.head and current.data == key:
                found = True
                self.head = current.next
            elif current.data == key:
                found = True
                previous.next = current.next
            else:
                previous = current
                current = current.next
        return current

    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

        while position < index:
            current = current.next
            position += 1
        
        return current


    def __repr__(self) -> str:
        nodes = []
        current = self.head
        while current:
            if current == self.head:
                nodes.append(f"head: {current}")
            elif current.next == None:
                nodes.append(f"tail: {current}")
            else:
                nodes.append(f"{current}")
            current = current.next

        return " --> ".join(nodes)

l = LinkedList()
l.add(21)
l.add(13)
l.add(99)
l.add(10)
print("base:", l)
l.insert(33, 1)
print("inserted 33:", l)
l.insert(87, 0)
print("inserted 87:", l)
l.remove(33)
print("removed 33:", l)

print("size:", l.size())
print("head:", l.head)
r = l.search(99)
print("search for 99:", r)