from linked_list import LinkedList

def split(linked_list):
    if linked_list is None or linked_list.head is None:
        left_half = linked_list
        right_half = None
        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size // 2

        mid_node = linked_list.node_at_index(mid - 1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next
        mid_node.next = None

        return left_half, right_half


def merge(left, right):
    merged = LinkedList()

    merged.add(0)
    current = merged.head
    
    left_head = left.head
    right_head = right.head

    while left_head or right_head:
        if left_head is None:
            current.next = right_head
            right_head = right_head.next
        elif right_head is None:
            current.next = left_head
            left_head = left_head.next
        else:
            left_data = left_head.data
            right_data = right_head.data
            if left_data < right_data:
                current.next = left_head
                left_head = left_head.next
            else:
                current.next = right_head
                right_head = right_head.next
        current = current.next
    
    head = merged.head.next
    merged.head = head

    return merged


def merged_sort(linked_list):
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merged_sort(left_half)
    right = merged_sort(right_half)

    return merge(left, right)


l = LinkedList()
l.add(10)
l.add(2)
l.add(44)
l.add(15)
l.add(100)
l.add(200)
l.add(1)

print(l)
print(merged_sort(l))