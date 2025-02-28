from markdown_blocks import markdown_to_blocks
import unittest
from markdown_blocks import (BlockType, 
                             block_to_block_type, 
                             markdown_to_blocks,
                             markdown_to_html_node,
                             )

class TestBlockType(unittest.TestCase):
    def test_block_to_block_type1(self):
        self.assertEqual(block_to_block_type("# Hello"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("```python\nprint('Hello')\n```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("> Hello"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("- Hello"), BlockType.ULIST)
        self.assertEqual(block_to_block_type("1. Hello"), BlockType.OLIST)
        self.assertEqual(block_to_block_type("Hello"), BlockType.PARAGRAPH)

    def test_block_to_block_type2(self):
        self.assertEqual(block_to_block_type("##### Hello"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("######### Hello"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("#######Hello"), BlockType.PARAGRAPH)
    
    def test_block_to_block_type3(self):
        self.assertEqual(block_to_block_type("```python\nprint('Hello')\n"), BlockType.PARAGRAPH)
    
    def test_block_to_block_type4(self):
        self.assertEqual(block_to_block_type("-Hello"), BlockType.PARAGRAPH)

    def test_block_to_block_type5(self):
        self.assertEqual(block_to_block_type("1. Hello"), BlockType.OLIST)
        self.assertEqual(block_to_block_type("1. Hello\n3. Hello"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("2. Hello\n3. Hello"), BlockType.PARAGRAPH)

    def test_block_to_block_types7(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.ULIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.OLIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
if __name__ == "__main__":
    unittest.main()


class TestSplitBlocks(unittest.TestCase):
    def test_split_blocks1(self):
        markdown = "This is a block of text.\n\nThis is another block of text."
        expected = ["This is a block of text.", "This is another block of text."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_split_blocks2(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_split_blocks3(self):
        test_markdown = """

    # Heading 1

    Paragraph text.

    * Item 1
    * Item 2

"""
        markdown_to_blocks(test_markdown)

def test_paragraphs(self):
    md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

def test_codeblock(self):
    md = """ """


    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_code(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )



if __name__ == "__main__":
    unittest.main()