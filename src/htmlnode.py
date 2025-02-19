
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else []

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not isinstance(self.props, dict):
            return ""
        if not self.props:
            return ""
        items = []
        for key, value in self.props.items():
            items.append(f' {key}="{value}"')
        return "".join(items)

    def __repr__(self):
        return f"HTMLNode({self.tag},{self.value},{self.children},{self.props})"

