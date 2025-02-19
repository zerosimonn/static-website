import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_noteq(self):
        node = TextNode("This is another text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)
    def test_noteq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_equrl(self):
        node = TextNode("This is another text node", TextType.BOLD, "url.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "url.com")
        self.assertNotEqual(node, node2)
    def test_url(self):
        node = TextNode("1", TextType.BOLD, None)
        self.assertIsNone(node.url)
    def test_repr(self):
        node = TextNode("1", TextType.BOLD, "url.com")
        self.assertEqual("TextNode(1, bold, url.com)", repr(node))

if __name__ == "__main__":
    unittest.main()
