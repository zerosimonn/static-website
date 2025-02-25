import unittest

from node_transformations import *  

class TestTextNode(unittest.TestCase):
    def test_transformation_bold(self):
        text_node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag,"b")
        self.assertEqual(html_node.value,"This is a text node")

    def test_transformation_italic(self):
        text_node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag,"i")
        self.assertEqual(html_node.value,"This is a text node")

    def test_transformation_notag(self):
        text_node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag,None)
        self.assertEqual(html_node.value,"This is a text node")

    def test_transformation_code(self):
        text_node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag,"code")
        self.assertEqual(html_node.value,"This is a text node")

    def test_transformation_link(self):
        text_node = TextNode("This is a text node", TextType.LINK, "bootdev.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag,"a")
        self.assertEqual(html_node.value,"This is a text node")
        self.assertEqual(html_node.props["href"],"bootdev.com")

    def test_transformation_notag(self):
        text_node = TextNode("This is alt text", TextType.IMAGE,"image-url.png")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag,"img")
        self.assertEqual(html_node.value,"")
        self.assertEqual(html_node.props["src"], "image-url.png")
        self.assertEqual(html_node.props["alt"], "This is alt text")

if __name__=="__main__":
    unittest.main()
