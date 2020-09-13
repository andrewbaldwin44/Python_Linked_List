import unittest

from linked_list import LinkedList, Element

class LinkedListElementTest(unittest.TestCase):
    def test_element_holds_value(self):
        new_element = Element(20)
        self.assertEqual(new_element.value, 20)

    def test_element_holds_next_element(self):
        first_element = Element(1)
        second_element = Element('some string')

        first_element.next_node = second_element
        self.assertEqual(first_element.next_node.value, second_element.value)

class SimpleLinkedListTest(unittest.TestCase):
    def test_empty_list_has_no_head(self):
        list = LinkedList()
        self.assertIs(list.head, None)

    def test_empty_list_has_no_tail(self):
        list = LinkedList()
        self.assertIs(list.tail, None)

    def test_push_element_to_list(self):
        list = LinkedList()
        list.push(50)

        self.assertEqual(list.to_array(), [50])

    def test_push_multiple_elements_to_list(self):
        list = LinkedList()
        list.push(50).push(1).push(20).push([1, 2, 3]).push('hello')

        self.assertEqual(list.to_array(), [50, 1, 20, [1, 2, 3], 'hello'])

    def test_push_existing_elements_to_list(self):
        list = LinkedList()

        first_element = Element([1, 2, 3])
        second_element = Element('cool')

        list.push(first_element).push(second_element)

        self.assertEqual(list.to_array(), [[1, 2, 3], 'cool'])

    def test_populated_list_has_head(self):
        list = LinkedList()

        list.push(5)

        self.assertEqual(list.head.value, 5)

    def test_populated_list_has_tail(self):
        list = LinkedList()

        list.push(5).push(10)

        self.assertEqual(list.tail.value, 10)

    def test_populated_list_has_size(self):
        list = LinkedList()

        list.push(5).push(10).push(20)

        self.assertEqual(len(list), 3)

    def convert_list_to_string(self):
        list = LinkedList()
        list.push(20).push(10).push([1, 2, 3])

        self.assertEqual(str(list), '( 20 ) -> ( 10 ) -> ( [1, 2, 3] ) -> ')

    def test_unshift_list(self):
        list = LinkedList()

        list.unshift(5)

        self.assertEqual(list.head.value, 5)

    def test_unshift_multiple_elements(self):
        list = LinkedList()

        list.unshift(5).unshift([1, 2, 3]).unshift('hello')

        self.assertEqual(list.to_array(), ['hello', [1, 2, 3], 5])

    def test_pop_list(self):
        list = LinkedList()

        list.push(5).push(10).push(20)

        self.assertEqual(list.pop().value, 20)

    def test_shift_list(self):
        list = LinkedList()

        list.push(5).push(10).push(20)

        self.assertEqual(list.shift().value, 5)

    def test_list_len_with_push_pop_unshift_and_shift(self):
        list = LinkedList()

        list.push(5).push(10).push(20).push(50).unshift(44)
        list.pop()
        list.shift()

        self.assertEqual(len(list), 3)

    def test_get_element_at_index(self):
        list = LinkedList()

        list.push(5).push(10).push(20).push(50)

        self.assertEqual(list.at(2).value, 20)

    def test_get_element_at_first_index(self):
        list = LinkedList()

        list.push(5).push(10).push(20).push(50)

        self.assertEqual(list.at(0).value, 5)

    def test_get_element_at_last_index(self):
        list = LinkedList()

        list.push(5).push(10).push(20).push(50)

        self.assertEqual(list.at(-1).value, 50)

    def test_get_element_at_negative_index(self):
        list = LinkedList()

        list.push(5).push(10).push(20).push(50)

        self.assertEqual(list.at(-3).value, 10)

    def test_get_element_at_negative_index(self):
        list = LinkedList()

        list.push(5).push(10).push(20).push(50)

        self.assertEqual(list.at(-3).value, 10)

    def test_finding_element_index(self):
        list = LinkedList()

        list.push(5).push(10).push(20).push(50)

        self.assertEqual(list.find(5), 0)

    def test_finding_non_existant_element(self):
        list = LinkedList()

        list.push(5).push(10).push(20).push(50)

        self.assertIs(list.find(4), None)

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == '__main__':
    unittest.main()
