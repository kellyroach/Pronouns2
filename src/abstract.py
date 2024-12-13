################################################################
#
#     abstract.py
#
################################################################

"""Outputs LaTeX/TikZ abstract tree diagrams to Manager.stream."""

from modern import *

class AbstractNode:
    def __init__(self, label, x=0.0, y=0.0):
        self.label = label
        self.x = x
        self.y = y
        self.width = modern_token_width(label)
        self.height = TEX_LINE_HEIGHT
        self.isolated = False
        self.children = []

################################################################
#abstract_diagram
################################################################

def abstract_diagram(tree) -> None:
    """Convert abstract syntax tree into LaTeX/TikZ diagram written to Manager.stream.
    
    Args:
        tree: A nested list representing a syntax tree structure
    """
    abstract_write_prolog()
    abstract_write_commands(tree)
    abstract_write_epilog()

def abstract_write_prolog() -> None:
    Manager.write("\\bigbreak\n")
    Manager.write("\\begin{minipage}{\\textwidth}\n")
    Manager.write("\\makebox[\\textwidth][c]{\n")
    Manager.write("\\begin{tikzpicture}\n")

def abstract_write_epilog() -> None:
    Manager.write("\\end{tikzpicture}\n")
    Manager.write("}\n")
    Manager.write("\\end{minipage}\n")
    Manager.write("\\bigbreak\n")

def abstract_write_commands(tree) -> None:
    """
    Write Tikz commands for tree rooted at node.
    
    Args:
        node: AbstractNode
    """
    node = abstract_position(tree)
    abstract_write_node_commands(node)
    abstract_write_draw_commands(node)

def abstract_write_node_commands(node) -> None:
    """
    Write Tikz \\\\node commands for tree rooted at node.
    
    Args:
        node: AbstractNode
    """
    # Write Tikz \node command for current node with its coordinates
    label = modern_token(tex_escape_str(node.label))
    Manager.write(f"\\node at ({node.x:.6f}, {node.y:.6f}) {{{label}}};\n")
    # Write Tikz \node commands for children
    for child in node.children:
        abstract_write_node_commands(child)

def abstract_write_draw_commands(node) -> None:
    """
    Write Tikz \\\\draw commands for tree rooted at node.
    
    Args:
        node: AbstractNode
    """
    # Each recursive call is responsible for drawing lines which form
    # a triangle between node and its children, if the node has children
    if len(node.children) > 0:
        # Write Tikz \draw commands for triangle below node.
        abstract_write_triangle(node)
        # Write Tikz \draw commands for children
        for child in node.children:
            abstract_write_draw_commands(child)

def abstract_write_triangle(node) -> None:
    """
    Write Tikz \\\\draw commands for triangle below node.
    
    Args:
        node: AbstractNode
    """
    children = node.children
    left = children[0]
    right = children[-1]
    padding = tex_str_width("~~~~~") if left.isolated else tex_str_width("~~")
    left_limit = left.x - (left.width / 2) - padding
    right_limit = right.x + (right.width / 2) + padding
    # Draw the top two slanting sides of the triangle
    y_top = node.y - (node.height / 2)
    y_base = left.y
    Manager.write(f"\\draw ({node.x:.6f},{y_top:.6f}) -- ({left_limit:.6f},{y_base:.6f});\n")
    Manager.write(f"\\draw ({node.x:.6f},{y_top:.6f}) -- ({right_limit:.6f},{y_base:.6f});\n")
    # Loop over adjacent pairs in children.
    # Draw line segments forming baseline of the triangle,
    # while avoiding drawing over child labels.
    n = len(children)
    space = 0.1
    for i in range(n + 1):
        if i == 0:
            x_left = left_limit
        else:
            left = children[i - 1]
            x_left = left.x + (left.width / 2) + space
        if i == n:
            x_right = right_limit
        else:
            right = children[i]
            x_right = right.x - (right.width / 2) - space
        Manager.write(f"\\draw ({x_left:.6f},{y_base:.6f}) -- ({x_right:.6f},{y_base:.6f});\n")

################################################################
#abstract_position
################################################################

def abstract_position(tree):
    """
    Position all nodes in a tree. Returns root node of positioned tree.
    tree: nested list representation [label, child1, child2, ...]
    """
    if isinstance(tree, str):  # Leaf node
        label = tree
        root = AbstractNode(label)
        return root
    label = tree[0]
    root = AbstractNode(label)
    # Create and position children
    max_depth = 0
    for child_tree in tree[1:]:
        child = abstract_position(child_tree)
        root.children.append(child)
        # Update max depth
        child_depth = max(abs(desc.y) for desc in get_all_descendants(child))
        max_depth = max(max_depth, child_depth)
    if len(root.children) == 1:
        child.isolated = True
    # Position children
    family_dist = tex_str_width("~~~~~~~~~")
    sibling_dist = tex_str_width("~~")
    right_limits = []  # Initialize right_limits to track right boundaries
    for i in range(len(root.children)):
        right = root.children[i]
        # Find minimum required dx
        dx = 0 if i == 0 else sibling_dist
        for d in range(int(max_depth) + 1):
            # Retrieve the right limit from the list, or break if out of bounds
            if d >= len(right_limits):
                break
            right_limit = right_limits[d]
            # Calculate the leftmost limit of the current child
            left_limit = abstract_limit(right, d, True)
            # Skip if no left limit is available
            if left_limit is None:
                break
            # Choose the appropriate distance based on the level `d`
            dist = sibling_dist if d == 0 else family_dist
            # Update dx to ensure enough spacing at this depth
            dx = max(dx, dist + right_limit - left_limit)
        # Position the right child with the calculated offset
        abstract_translate(right, dx, -3.0 * TEX_LINE_HEIGHT)
        # Update right_limits with the new right boundaries of the current child
        for d in range(int(max_depth) + 1):
	    # Rightmost limit of the current child
            right_limit = abstract_limit(right, d, False)
            if right_limit is None:
                break
            # Extend or update the right_limits list as needed
            if len(right_limits) <= d:
                right_limits.append(right_limit)
            else:
                right_limits[d] = max(right_limits[d], right_limit)
    # Center children under parent
    if root.children:
        total_shift = -0.5 * (root.children[-1].x - root.children[0].x)
        for child in root.children:
            abstract_translate(child, total_shift, 0)
    return root

def get_all_descendants(node):
    """Helper function to get all descendants of a node, including the node itself."""
    result = [node]
    for child in node.children:
        result.extend(get_all_descendants(child))
    return result

def abstract_translate(node, dx, dy):
    """Translate a node and all its descendants by (dx, dy)."""
    node.x += dx
    node.y += dy
    for child in node.children:
        abstract_translate(child, dx, dy)

def abstract_descendant(node, depth, find_leftmost):
    """
    Find leftmost/rightmost descendant at given depth.
    Returns descendant.
    """
    if depth == 0:
        return node
    if depth < 0 or not node.children:
        return None
    children = node.children if find_leftmost else reversed(node.children)
    for child in children:
        descendant = abstract_descendant(child, depth - 1, find_leftmost)
        if descendant is not None:
            return descendant
    return None

def abstract_limit(node, depth, find_leftmost):
    """Calculate leftmost/rightmost limit at given depth."""
    descendant = abstract_descendant(node, depth, find_leftmost)
    if descendant is None:
        return None
    padding = tex_str_width("~~~~~") if descendant.isolated else tex_str_width("~~")
    if find_leftmost:
        return descendant.x - (descendant.width / 2) - padding
    else:
        return descendant.x + (descendant.width / 2) + padding
