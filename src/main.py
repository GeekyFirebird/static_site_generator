from textnode import TextNode, TextType
import os, shutil

def main():
    print(TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev"))

def recursive_function(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    

main()

