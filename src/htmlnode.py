class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        new_string = ""
        if self.props is None:
            return new_string
        for k, v in self.props.items():
            new_string += f' {k}="{v}"'
        return new_string
    
    def __repr__(self):
        return f"HTMLNode: {self.tag} {self.value} {self.children} {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Must Have A Value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode: {self.tag} {self.value} {self.props}"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Missing a tag")
        if self.children is None:
            raise ValueError("Missing value for children") 
        child_string = ""
        for each in self.children:
            child_string += each.to_html()
        full_string = f"<{self.tag}{self.props_to_html()}>{child_string}</{self.tag}>"
        return full_string
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"