import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node1 = HTMLNode("tag","value","children", {"href": "https://example.com"} )
    def test_props_to_html(self):
        node1 = HTMLNode("tag","value","children",{"href": "https://example.com", "target": "_blank"} )
        print(node1)
    
if __name__ == "__main__":
    unittest.main()
