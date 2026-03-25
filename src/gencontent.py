from markdown_blocks import markdown_to_html_node

import os


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")

# def extract_title(markdown):
#     if markdown.startswith("#"):
#         title = markdown.split("# ").strip()
#         return title

def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)
    
# def generate_page(from_path, template_path, dest_path):
#     if not os.path.exists(dest_path): 
#         os.mkdir(dest_path)

#     print(f"Generating page from {from_path} to {dest_path} using template_path")
#     read_from = from_path.read()
#     read_template = template_path.read()
#     html = markdown_to_html_node(read_from).to_html()
#     title = extract_title(read_from)
#     update_html = read_template.replace("{{ Title }}", title).replace("{{ Content }}", html)
#     f = open(dest_path, "w")
#     f.write(update_html)
#     f.close()