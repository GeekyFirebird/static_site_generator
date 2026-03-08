import unittest

from htmlnode import HTMLNode


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