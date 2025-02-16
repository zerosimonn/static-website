from textnode import TextNode, TextType

def main():
    new_object = TextNode("eerst",TextType.BOLD,"drie.com")
    node1 = TextNode("eerst", TextType.BOLD, "drie.com")
    node2 = TextNode("eerst", TextType.BOLD, "drie.com")
    node3 = TextNode("tweede", TextType.ITALIC, None)

    print(node1 == node2)  # Should output: True
    print(node1 == node3)  # Should output: False
    print(new_object)

main()

