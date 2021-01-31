class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __len__(self):
        return len(tuple(iter(self)))

    def __repr__(self):
        return "->".join([str(item) for item in self])

    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise ValueError("list index out of range")
        for i, node in enumerate(self):
            if i == index:
                return node

    def __setitem__(self, index, data):
        if not 0 <= index < len(self):
            raise ValueError("list index out of range")
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        current_node.data = data

    def insert_head(self, data):
        self.insert_nth(0, data)

    def insert_tail(self, data):
        self.insert_nth(len(self), data)

    def insert_nth(self, index, data):
        if not 0 <= index <= len(self):
            raise ValueError("list index out of range")
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            for _ in range(index-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

    def print_list(self):
        print(self)

    def delete_head(self):
        return self.delete_nth(0)

    def delete_tail(self):
        return self.delete_nth(len(self)-1)

    def delete_nth(self, index: int = 0):
        if not 0 <= index < len(self):
            raise ValueError("list index out of range")
        deleted_node = self.head  # this is the default one
        if index == 0:
            self.head = self.head.next
        else:
            node = self.head
            for _ in range(index-1):
                node = node.next
            deleted_node = node.next
            node.next = node.next.next
        return deleted_node.data

    def is_empty(self):
        return self.head is None

    def reverse(self):
        current = self.head
        previous = None

        while current:
            next_current = current.next
            current.next = previous
            previous = current
            current = next_current
        self.head = previous


def test_singly_linked_list():
    linked_list = SinglyLinkedList()
    assert linked_list.is_empty() is True

    try:
        linked_list.delete_head()
        assert False
    except ValueError:
        assert True

    for i in range(10):
        assert len(linked_list) == i
        linked_list.insert_nth(i, i+1)
    assert str(linked_list) == "->".join([str(x) for x in range(1, 11)])

    linked_list.insert_head(0)
    linked_list.insert_tail(11)
    assert str(linked_list) == "->".join([str(x) for x in range(12)])

    assert linked_list.delete_head() == 0
    assert linked_list.delete_nth(9) == 10
    assert linked_list.delete_tail() == 11
    assert len(linked_list) == 9
    assert str(linked_list) == "->".join([str(x) for x in range(1, 10)])

    assert all([linked_list[x-1] == x for x in range(1, 10)]) is True

    for i in range(0, 9):
        linked_list[i] = -i
    assert all([linked_list[x] == -x for x in range(0, 9)]) is True


if __name__ == "__main__":
    test_singly_linked_list()
