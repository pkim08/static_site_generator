import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_none(self):
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single_prop(self):
        node = HTMLNode(props={"href": "https://google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://google.com"')
        
    def test_props_to_html_empty_dict(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_multiple_props(self):
        node = HTMLNode(props={"href": "https://google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://google.com" target="_blank"')

    def test_leaf_to_html(self):
        leaf_node = LeafNode("p", "I like being a paragraph")
        self.assertEqual(leaf_node.to_html(), "<p>I like being a paragraph</p>")
	    
    def test_parent_to_html_example(self):
        node = ParentNode("p", 
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
    
    def test_single_child(self):
        node = ParentNode(
            "div",
            [LeafNode("span", "Hello")]
        )
        self.assertEqual(node.to_html(), "<div><span>Hello</span></div>")

    def test_nested_parents(self):
        node = ParentNode(
            "section",
            [
                ParentNode(
                    "article",
                    [
                        LeafNode("h1", "Title"),
                        LeafNode("p", "Content")
                    ]
                )
            ]
        )
        self.assertEqual(node.to_html(), "<section><article><h1>Title</h1><p>Content</p></article></section>")

    def test_missing_tag(self):
        node = ParentNode(
            None,
            [LeafNode("p", "Test")]
        )
        

    def test_empty_children(self):
        node = ParentNode(
            "div",
            []
        )
 
    def test_mixed_with_props(self):
        node = ParentNode(
            "nav",
            [
                LeafNode("a", "Home", {"href": "/home"}),
                LeafNode(None, " | "),
                LeafNode("a", "About", {"href": "/about"})
            ]
        )
        self.assertEqual(node.to_html(), '<nav><a href="/home">Home</a> | <a href="/about">About</a></nav>')

if __name__ == "__main__":
    unittest.main()
