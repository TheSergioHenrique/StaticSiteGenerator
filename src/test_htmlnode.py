import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_node_no_properties(self):
        node = HTMLNode(tag="div", value="Content")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Content")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})
        self.assertEqual(node.props_to_html(), "")

    def test_node_one_property(self):
        node = HTMLNode(tag="div", value="Content", props={"class": "my-class"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Content")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "my-class"})
        self.assertEqual(node.props_to_html(), ' class="my-class"')

    def test_node_multiple_properties(self):
        node = HTMLNode(tag="div", value="Content", props={"class": "my-class", "id": "my-id"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Content")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "my-class", "id": "my-id"})
        self.assertEqual(node.props_to_html(), ' class="my-class" id="my-id"')


    if __name__ == "__main__":
        unittest.main()
