class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def create_element(self, value):
        return value if isinstance(value, Element) else Element(value)

    def empty_list(self):
        self.head = None
        self.tail = None

    def valid(self, index):
        if index < 0:
            index = self.size - abs(index)

        return index if self.size >= index and index >= 0 else None

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

        self.size += 1

        return self

    def unshift(self, value):
        new_element = self.create_element(value)

        new_element.next_node = self.head
        self.head = new_element

        self.size += 1

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
                self.empty_list()

            self.size -= 1

            return current_node

    def shift(self):
        if self.head:
            current_node = self.head

            if self.head.next_node:
                self.head = self.head.next_node
            else:
                self.empty_list()

            self.size -= 1

            return current_node

    def at(self, index):
        index = self.valid(index)

        if self.head and index is not None:
            current_index = 0
            current_node = self.head

            while current_index != index:
                current_index += 1
                current_node = current_node.next_node

            return current_node

    def find(self, value):
        if self.head:
            current_node = self.head
            current_index = 0

            while current_node:
                if current_node.value == value:
                    return current_index

                current_node = current_node.next_node
                current_index += 1

    def is_containing(self, value):
        return True if self.find(value) is not None else False

    def insert_at(self, value, index):
        valid_index = self.valid(index)

        if valid_index is None:
            return None
        elif valid_index == 0:
            return self.unshift(value)
        elif valid_index == self.size - 1:
            return self.push(value)
        else:
            new_element = self.create_element(value)

            if (index > 0):
                valid_index -= 1

            previous_node = self.at(valid_index)
            current_node = previous_node.next_node

            previous_node.next_node = new_element
            new_element.next_node = current_node

            self.size += 1

        return self

    def remove_at(self, index):
        valid_index = self.valid(index)

        if valid_index is None:
            return None
        elif valid_index == 0:
            self.shift()
        elif valid_index == self.size - 1:
            self.pop()
        else:
            valid_index -= 1

            previous_node = self.at(valid_index)
            current_node = previous_node.next_node

            previous_node.next_node = current_node.next_node

            self.size -= 1

        return self

    def reverse(self):
        if self.head:
            previous_node = None
            current_node = self.head
            next_node = None

            while current_node:
                next_node = current_node.next_node
                current_node.next_node = previous_node

                previous_node = current_node
                current_node = next_node

            self.head = previous_node

            return self

    def to_array(self):
        output = []

        if self.head:
            current_node = self.head

            while current_node:
                output.append(current_node.value)
                current_node = current_node.next_node

        return output

    def __len__(self):
        return self.size

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
