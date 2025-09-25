import unittest
from block_markdown import (
    markdown_to_html_node,
    extract_title
)


class TestMarkdownToHTML(unittest.TestCase):
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

    def test_headings(self):
        md = """
# this is a heading

###### this is another one
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is a heading</h1><h6>this is another one</h6></div>",
        )

    def test_quotes(self):
        md = """
> This is a
> quote block

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote block</blockquote></div>",
        )

    def test_ulist(self):
        md = """
* This is a
* list item

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a</li><li>list item</li></ul></div>",
        )

    def test_olist(self):
        md = """
1. This is an
2. ordered list

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is an</li><li>ordered list</li></ol></div>",
        )

    def test_extract_title(self):
        md = """
# This is a title

This is a paragraph
"""
        title = extract_title(md)
        self.assertEqual(title, "This is a title")


if __name__ == "__main__":
    unittest.main()