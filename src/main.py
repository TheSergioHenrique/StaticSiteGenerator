from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        split_nodes = []
        parts = old_node.text.split(delimiter)
        
        if len(parts) % 2 == 0:
            raise ValueError("Invalid markdown syntax: missing closing delimiter")
            
        for i, part in enumerate(parts):
            if part == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(part, TextType.TEXT))
            else:
                split_nodes.append(TextNode(part, text_type))
        new_nodes.extend(split_nodes)
        
    return new_nodes
