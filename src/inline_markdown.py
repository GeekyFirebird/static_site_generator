import re

from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_list.append(old_node)
            continue
        if old_node.text.count(delimiter) % 2 != 0:
             raise Exception("Invalid Markdown Syntax") 
        split_list = old_node.text.split(delimiter)
        for i in range(len(split_list)):
            if split_list[i] == "":
                continue
            if i == 0:
                new_list.append(TextNode(split_list[i], TextType.TEXT))
            elif i % 2:
                new_list.append(TextNode(split_list[i], text_type))
            else:
                new_list.append(TextNode(split_list[i], TextType.TEXT))
    return new_list

def extract_markdown_images(text):
    image_match = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return image_match

def extract_markdown_links(text):
    link_match = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return link_match
