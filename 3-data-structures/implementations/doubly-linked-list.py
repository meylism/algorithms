class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.data
            curr = curr.next

    def __str__(self):
        return "->".join([str(x) for x in self])

    def __len__(self):
        return len(tuple(iter(self)))

    def insert_at_head(self, data):
        self.insert_at_nth(0, data)

    def insert_at_tail(self, data):
        self.insert_at_nth(len(self), data)

    def insert_at_nth(self, index, data):
        if not 0 <= index <= len(self):
            raise ValueError("list index out of range")
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        elif index == len(self):
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            curr = self.head
            for _ in range(index-1):
                curr = curr.next
            new_node.prev = curr
            new_node.next = curr.next
            curr.next = new_node

    def delete_head(self):
        return self.delete_nth(0)

    def delete_tail(self):
        return self.delete_nth(len(self)-1)

    def delete_nth(self, index):
        if not 0 <= index < len(self):
            raise ValueError("list index out of range")
        deleted_node = self.head
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
        elif index == len(self)-1:
            deleted_node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            curr = self.head
            for _ in range(index-1):
                curr = curr.next
            deleted_node = curr.next
            temp = curr
            curr = curr.next.next
            curr.prev = temp
        return deleted_node.data

    def delete(self, data):
        curr = self.head
        while curr.data != data:
            if curr.next:
                curr = curr.next
            else:
                return "given data doesn't exist in the list"
        if curr == self.head:
            self.delete_head
        elif curr == self.tail:
            self.delete_tail()
        else:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
        return data

    def is_empty(self):
        return len(self) == 0


def test_doubly_linked_list():
    linked_list = DoublyLinkedList()
    assert linked_list.is_empty() is True
    assert str(linked_list) == ""

    try:
        linked_list.delete_head()
        assert False
    except ValueError:
        assert True

    try:
        linked_list.delete_tail()
        assert False
    except ValueError:
        assert True

    for i in range(10):
        assert len(linked_list) == i
        linked_list.insert_at_nth(i, i+1)
    assert str(linked_list) == "->".join([str(x) for x in range(1, 11)])

    linked_list.insert_at_head(0)
    linked_list.insert_at_tail(11)
    assert str(linked_list) == "->".join([str(x) for x in range(12)])

    assert linked_list.delete_head() == 0
    assert linked_list.delete_nth(9) == 10
    assert linked_list.delete_tail() == 11
    assert len(linked_list) == 9
    assert str(linked_list) == "->".join([str(x) for x in range(1, 10   )])


if __name__ == "__main__":
    test_doubly_linked_list()
