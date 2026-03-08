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
