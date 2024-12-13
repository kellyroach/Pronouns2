################################################################
#
#    chaining.py
#
################################################################

"""Outputs LaTeX/TikZ chaining diagrams to Manager.stream."""

import math
import sys
import numpy as np
from modern import *
from spread import *

################################################################
#Tikz Chaining Diagrams
################################################################

def chaining_diagram(nnodes: list[Node]) -> None:
    """Creates a TikZ-CD diagram showing node chains with
    connecting arrows and dotted lines between related nodes.

    Args:
        nnodes (list[Node]): List of nodes to visualize in the diagram
    """
    # Begin Tikz diagram
    chaining_begin()
    # Write nodes and dotted lines
    labels = chaining_labels(nnodes)
    chaining_write(labels)
    # Write arrows
    chaining=chaining_chaining(nnodes)
    coords=chaining_coords(chaining)
    inverses=chaining_inverses(chaining)
    chaining_sort(inverses,coords)
    chaining_inverses_write(inverses, coords, labels)
    # End Tikz diagram
    chaining_end()

def chaining_write(rows: list[list[str]]) -> None:
    widths = chaining_column_widths(rows[1])
    spacing = 0.802661
    total_width = sum(widths) + (len(widths) - 1) * spacing
    # Print S node at top
    Manager.write(f"\\node (S) at ({(total_width/2):.6f},0.000000) {{S}};\n")
    # Process each row and connections
    y_spacing = -3.0 * TEX_LINE_HEIGHT
    for i, row in enumerate(rows):
        chaining_row(row, widths, spacing=spacing, y=y_spacing*(i+1))
        if i == 0:
            chaining_triangular_shape(row)
        elif i > 0:
            chaining_vertically_connect(rows[i-1], row)

def chaining_begin():
    # Print preamble
    Manager.write("\\bigbreak\n")
    Manager.write("\\begin{minipage}{\\textwidth}\n")
    Manager.write("\\makebox[\\textwidth][c]{\n")
    Manager.write("\\begin{tikzpicture}[\n")
    Manager.write("    every node/.style={align=center},\n")
    Manager.write("    dotted line/.style={draw, dotted, thick},\n")
    Manager.write("    curved arrow/.style={draw, thick, -{Latex[bend]}},\n")
    Manager.write("    ]\n")

def chaining_end():
    # Close the environment
    Manager.write("\\end{tikzpicture}\n")
    Manager.write("}\n")
    Manager.write("\\end{minipage}\n")
    Manager.write("\\bigbreak\n")

def chaining_column_widths(row: list[str]) -> list[float]:
    """Calculate width of each column based on second row."""
    return [tex_str_width(s) for s in row]

def chaining_row(row: list[str], widths: list[float], spacing: float, y: float) -> None:
    """Output nodes for a single row at height y."""
    left_edge = 0
    for j, s in enumerate(row):
        if s:  # if string is non-empty
            x = left_edge + 0.5 * widths[j]
            label = modern_token(tex_escape_str(s))
            Manager.write(f"\\node ({s}) at ({x:.6f},{y:.6f}) {{{label}}};\n")
        left_edge = left_edge + widths[j] + spacing

def chaining_triangular_shape(row: list[str]) -> None:
    """Draw dotted lines from S to first and last nodes of row,
    plus horizontal connections in that row."""
    # Connect S to first and last nodes
    Manager.write(f"\\draw[dotted line] (S) -- ({row[0]});\n")
    Manager.write(f"\\draw[dotted line] (S) -- ({row[-1]});\n")
    # Connect nodes horizontally
    chaining_horizontally_connect(row)

def chaining_horizontally_connect(row: list[str]) -> None:
    """Draw dotted lines between adjacent non-empty nodes in a row."""
    for i in range(len(row)-1):
        if row[i] and row[i+1]:  # if both strings are non-empty
            Manager.write(f"\\draw[dotted line] ({row[i]}) -- ({row[i+1]});\n")

def chaining_vertically_connect(row1: list[str], row2: list[str]) -> None:
    """Draw dotted lines between corresponding non-empty nodes in adjacent rows."""
    for s1, s2 in zip(row1, row2):
        if s1 and s2:  # if both strings are non-empty
            Manager.write(f"\\draw[dotted line] ({s1}) -- ({s2});\n")

################################################################
#chaining_nodes etc.
################################################################

def chaining_labels(nnodes: list[Node]) -> list[list[str]]:
    rows = [chaining_labels_row(row) for row in chaining_nodes(nnodes)]
    return rows

def chaining_labels_row(row: list[Node]) -> list[str]:
    row = [view_label(node) for node in row]
    return row

def chaining_chaining(nnodes: list[Node]) -> list[list[Node]]:
    return chaining_nodes(nnodes)[1:]

def chaining_nodes(nnodes: list[Node]) -> list[list[Node]]:
    columns = [chaining_nodes_column(nnode) for nnode in nnodes]
    rows = view_transpose_any(columns)
    return rows

def chaining_nodes_column(nnode: Node) -> list[Node]:
    column = []
    current = nnode
    while current is not None:
        column.append(current)
        current = current.col_link
    return column

################################################################
#Chaining Table arrows representing chains
################################################################

def chaining_inverses_write(inverses: dict[int, list[int]],
                            coords: dict[int, list[int]],
                            labels: list[list[str]]) -> None:
    # Writes Tikz \draw commands for each key-value pair in inverses.
    for p, qs in inverses.items():
        chaining_inverses_bucket_write(p, qs, coords, labels)

def chaining_inverses_bucket_write(p: int,
                                   qs: list[int],
                                   coords: dict[int, list[int]],
                                   labels: list[list[str]]) -> None:
    # Writes a subset of Tikz \draw commands for each q in qs linking to p.
    in_angles = [chaining_angle(p, q, coords) for q in qs]
    #in_angles = spread(in_angles, 0.5)
    in_angles = spread(in_angles, Manager.chaining_rho)
    for q, in_angle in zip(qs, in_angles):
        # Calculate the "out" angle from q to p
        out_angle = chaining_angle(q, p, coords)
        # Convert angles to compass directions
        out_direction = spread_compass_direction(out_angle)
        in_direction = spread_compass_direction(in_angle)
        # Get labels for q and p
        label_q = chaining_label(q, coords, labels)
        label_p = chaining_label(p, coords, labels)
        # Write Tikz \draw command to Manager.stream
        out_degrees = math.degrees(out_angle)
        in_degrees = math.degrees(in_angle)
        # Single output line broken up into easier-to-read code.
        Manager.write(f"\\draw[curved arrow] ({label_q}.{out_direction}) ")
        Manager.write(f"to [out={out_degrees:.2f},in={in_degrees:.2f}] ")
        Manager.write(f"({label_p}.{in_direction});\n")

def chaining_coords(chaining: list[list[Optional['Node']]]) -> dict[int, list[int]]:
    # Create a dictionary mapping each node's number to its
    # coordinates [i, j] in the chaining_chaining matrix.
    coords = {}
    for i, row in enumerate(chaining):
        for j, node in enumerate(row):
            if node is not None:  # Only store coordinates for actual nodes
                coords[node.number] = [i, j]
    return coords

def chaining_inverses(chaining: list[list[Optional['Node']]]) -> dict[int, list[int]]:
    # Create a dictionary mapping each node's number to a list
    # of node numbers that reference it via chain_link.
    inverses = {}
    for row in chaining:
        for node in row:
            if node is not None and node.chain_link is not None:
                # Get the target node's number from the chain_link
                target_number = node.chain_link.number
                # Initialize the target's entry in inverses if it doesn't exist
                if target_number not in inverses:
                    inverses[target_number] = []
                # Append the current node's number to the target's list of inverses
                inverses[target_number].append(node.number)
    return inverses

def chaining_angle(p: int, q: int, coords: dict[int, list[int]]) -> float:
    # Calculate the angle from node p to node q based on their
    # coordinates in chaining_chaining.
    # Retrieve the coordinates of nodes p and q
    i, j = coords[p]
    k, l = coords[q]
    #print(f"[l-j,k-i] = [{l-j},{k-i}]")
    # Calculate the angle using spread_atan2 with the specified scaling
    angle = spread_atan2(3.0 * TEX_LINE_HEIGHT * (l - j), -1.918167 * (k - i))
    return angle

def chaining_distance_squared(p: int, q: int, coords: dict[int, list[int]]) -> float:
    # Calculate the squared distance between node p and node q
    # based on their coordinates in chaining_chaining.
    # Retrieve the coordinates of nodes p and q
    i, j = coords[p]
    k, l = coords[q]
    # Calculate the squared distance using the specified scaling factors
    dx = 1.918167 * (k - i)
    dy = 3.0 * TEX_LINE_HEIGHT * (l - j)
    distance_squared = dx * dx + dy * dy
    return distance_squared

def chaining_sort_list(qs: list[int], p: int, coords: dict[int, list[int]]) -> list[int]:
    # Sorts a list of node numbers `qs` based on the angle and distance from a node `p`.
    # Define the key function for sorting by angle first, then by distance squared
    def sort_key(q):
        # Primary: angle in reverse direction (q -> p)
        angle = chaining_angle(p, q, coords)
        # Secondary: distance squared as a tie-breaker
        distance = chaining_distance_squared(p, q, coords)
        return (angle, distance)
    # Sort qs based on the defined sort_key function
    answer = sorted(qs, key=sort_key)
    answer.reverse()
    return answer

def chaining_sort(inverses: dict[int, list[int]], coords: dict[int, list[int]]) -> None:
    # Sorts each list of node numbers in `inverses` based on
    # angle and distance to the reference node.
    for q in inverses:
        # Sort the list of node numbers linked to q
        inverses[q] = chaining_sort_list(inverses[q], q, coords)

def chaining_label(p: int, coords: dict[int, list[int]], labels: list[list[str]]) -> str:
    i, j = coords[p]
    return labels[1:][i][j]
