import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a paragraph")
        node2 = HTMLNode("p", "This is a paragraph")
        self.assertEqual(node.tag, node2.tag)

    def test_props(self):
        node = HTMLNode("a", "This is a link", None, {"href": "https://www.google.com", "target": "_blank"})
        expected_props = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_props)

    def test_print(self):
        node = HTMLNode("a", "This is a link", None, {"href": "https://www.google.com", "target": "_blank"})
        print(node)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_repr_a(self):
        node = LeafNode("a", "This is a new link", {"href": "https://www.google.com", "target": "_blank"})
        print(node)