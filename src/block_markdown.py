import re

from textnode import TextNode, TextType

def markdown_to_blocks(markdown):
    list_markdown = []
    split_markdown = markdown.split("\n\n")
    for each in split_markdown:
        if each == "":
            continue
        list_markdown.append(each.strip())
    return list_markdown
