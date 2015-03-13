o = object

class Node(o):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    @classmethod
    def create_node(cls, data):
        return cls(data)


class LinkedList(o):
    def __init__(self, head=None):
        self.head = head

    def print_list(self):
        """
        Prints all elements of List
        O(n)
        """
        if self.head is None:
            return
        current_node = self.head
        while True:
            print current_node.data
            if current_node.next is None:
                break
            current_node = current_node.next

    def add_node(self, data):
        """
        This adds Node at the beginning of List
        This is O(1)
        """
        node = Node.create_node(data)
        if self.head is None:
            self.head = node
            return
        existing_head = self.head
        node.next = existing_head
        self.head = node

    def append_node(self, data):
        """
        Adds Node at end of List
        This is O(n)
        """
        new_node = Node.create_node(data)
        if self.head is None:
            # If List is empty
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

def create_list():
    return LinkedList()