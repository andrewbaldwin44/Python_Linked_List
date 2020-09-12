class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def create_element(self, value):
        return value if isinstance(value, Element) else Element(value)

    def push(self, value):
        new_element = self.create_element(value)

        if not self.head:
            self.head = new_element
        elif not self.tail:
            self.head.next_node = new_element
            self.tail = new_element
        else:
            current_tail = self.tail

            current_tail.next_node = new_element
            self.tail = new_element

        return self

    def shift(self, value):
        new_element = self.create_element(value)

        new_element.next_node = self.head
        self.head = new_element

        return self

    def pop(self):
        if self.head:
            previous_node = None
            current_node = self.head

            while current_node.next_node:
                previous_node = current_node
                current_node = current_node.next_node

            if previous_node:
                previous_node.next_node = None
                self.tail = previous_node
            else:
                self.head = None
                self.tail = None

            return current_node

    def to_array(self):
        output = []

        if self.head:
            current_node = self.head

            while current_node:
                output.append(current_node.value)
                current_node = current_node.next_node

        return output

    def __str__(self):
        output = ""

        if self.head:
            current_node = self.head

            while current_node:
                output += f"( {current_node.value} ) -> "
                current_node = current_node.next_node

        else:
            output += "( ) ->"

        return output

class Element:
    def __init__(self, value):
        self.value = value
        self.next_node = None
