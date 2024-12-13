################################################################
#
#     demo.py
#
################################################################

"""Writes demo output for all examples to Manager.stream."""

import sys
from examples import *
from table_interp import *
from table_proc import *

################################################################
#demo
################################################################

def demo(numbers = None, **kwargs):
    """Runs demo_example() on all examples in numbers sequentially.

    Args:
        numbers (optional): None, str, or list[str] of keys in example_dict
        kwargs: other key-value arguments accepted by Manager.set_state
    """
    numbers = demo_numbers(numbers)
    with Manager.manager:
        # Update the state of the singleton Manager
        Manager.set_state(**kwargs)
        # Reset the summary
        Summary.reset()
        # Iterate through all examples
        for number in numbers:
            if Manager.file_type == FileType.TEX:
                Manager.write("\n")
                Manager.write("\\clearpage\n")
            demo_example(number, **kwargs)
        if len(numbers) > 1:
            # Write summary and lexicon tables
            demo_write_summary_table()
            demo_write_lexicon_table()

def demo_numbers(numbers) -> list[str]:
    """Coerce input numbers to list[str]

    Args:
        numbers: None, str, or list[str] of keys in example_dict

    Returns:
        list[str]: numbers coerced to list[str]
    """
    if numbers is None:
        return list(example_dict.keys())
    if isinstance(numbers, str):
        return [numbers]
    if isinstance(numbers, list):
        return numbers
    raise TypeError(f"numbers must be None, str, or list, not {type(numbers)}")

def demo_example(number: str, **kwargs):
    """Processes and displays analysis of a single example
    sentence, showing parse tree structure, features, nodes,
    chains, and interpretations.

    Args:
        number (str): Example sentence identifier in example_dict
        kwargs: other key-value arguments accepted by Manager.set_state
    """
    with Manager.manager:
        # Update the state of the singleton Manager
        Manager.set_state(**kwargs)
        if Manager.minimum and (Manager.stream != sys.stdout):
            Manager.set_state(info=True,
                              features_table=False,
                              abstract_diagram=False,
                              nodes_after_chaining=False,
                              nodes_table=False,
                              chaining_diagram=False,
                              chaining_table=False,
                              interpretations_table=True,
                              summary_table=False,
                              lexicon_table=False)
        # Process the example sentence
        ex = example(number)
        sentence = ex[0]
        csn = ex[1]
        Node.set_tree(parse(csn))
        # Write the example number and sentence
        demo_write_number_sentence(number, sentence)
        demo_write_abstract_diagram(csn)
        demo_write_nodes_after_parse()
        nnodes = tree_n_nodes(Node.tree())
        demo_write_features_table(nnodes)
        chaining(nnodes)
        demo_write_nodes_after_chaining()
        demo_write_chaining_diagram(nnodes)
        demo_write_chaining_table(nnodes)
        interps = interpret(nnodes)
        demo_write_interpretations_table(interps)
        n_interps = len(interps)
        demo_absorb(number, n_interps)

def demo_absorb(number: str, n_interps: int):
    # Absorb n_interps statistic for sentence "number" into Summary.
    ex = example(number)
    sentence = ex[0]
    judgement = sentence[0] if sentence and sentence[0] in {"*", "?"} else " "
    # We're going a little too far overboard with some crude assumptions,
    # but the idea is that our code is "correct" when the discovered number
    # of interpretations ("n_interps") seems to be in line with the "judgement".
    #
    # meaningless      (== 0 interps)
    # meaningful       (== 1 interp)
    # ambiguous        (>= 2 interps)
    # correct          (no * needs 1, * needs 0, ? needs 0-1)
    if n_interps == 0:
        Summary.meaningless += 1
        if judgement != " ":
            Summary.correct += 1
    elif n_interps == 1:
        Summary.meaningful += 1
        if judgement != "*":
            Summary.correct += 1
    else:
        Summary.ambiguous += 1
    Summary.total += 1

def demo_write_number_sentence(number: str, sentence: str):
    if Manager.minimum:
        # Minimal output
        Manager.write(f"({number}) {sentence}\n")
    elif Manager.file_type == FileType.TXT:
        Manager.write("\n")
        Manager.write("################################################################\n")
        Manager.write("#\n")
        Manager.write(f"#     ({number}) {sentence}\n")
        Manager.write("#\n")
        Manager.write("################################################################\n")
    elif Manager.file_type == FileType.TEX:
        Manager.write("\n")
        Manager.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
        Manager.write("%\n")
        Manager.write(f"%     ({number}) {sentence}\n")
        Manager.write("%\n")
        Manager.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
        Manager.write("\n")
        Manager.write(f"\\section*{{({number}) {sentence}}}\n")
        Manager.write(f"\\addcontentsline{{toc}}{{section}}{{({number}) {sentence}}}\n")
        Manager.write("\n")
        Manager.write("\\bigbreak\n")
        Manager.write("\\begin{enumerate*}\n")
        Manager.write(f"\\item[({number})] {sentence}\n")
        Manager.write("\\end{enumerate*}\n")
        Manager.write("\\bigbreak\n")

def demo_write_abstract_diagram(tree):
    if Manager.info and Manager.abstract_diagram:
         if Manager.file_type == FileType.TEX:
              abstract_diagram(tree)

def demo_write_features_table(nnodes: list[Node]):
    if Manager.info and Manager.features_table:
        if Manager.file_type == FileType.TXT:
            Manager.write("\n")
            txt_features(nnodes)
        elif Manager.file_type == FileType.TEX:
            Manager.write("\n")
            latex_features(nnodes)

def demo_write_nodes_after_parse():
    if Manager.debug and Manager.nodes_after_parse:
        nodes = tree_nodes(Node.tree())
        demo_write_nodes_table(nodes)

def demo_write_nodes_after_chaining():
    if Manager.info and Manager.nodes_after_chaining:
        nodes = tree_nodes(Node.tree())
        demo_write_nodes_table(nodes)

def demo_write_nodes_table(nodes: list[Node]):
    if Manager.info and Manager.nodes_table:
        if Manager.file_type == FileType.TXT:
            Manager.write("\n")
            txt_nodes(nodes)
        elif Manager.file_type == FileType.TEX:
            Manager.write("\n")
            latex_nodes(nodes)

def demo_write_chaining_diagram(nnodes: list[Node]):
    if Manager.info and Manager.chaining_diagram:
        if Manager.file_type == FileType.TEX:
            Manager.write("\n")
            chaining_diagram(nnodes)

def demo_write_chaining_table(nnodes: list[Node]):
    if Manager.info and Manager.chaining_table:
        if Manager.file_type == FileType.TXT:
            Manager.write("\n")
            txt_chaining(nnodes)
        elif Manager.file_type == FileType.TEX:
            Manager.write("\n")
            latex_chaining(nnodes)

def demo_write_interpretations_table(interps: list[list[list[Node]]]):
    if Manager.minimum:
        # Minimal output implies (Manager.stream = sys.stdout),
        # arranged by lines of code in "function demo_example".
        Manager.write(f"{view_interps(interps)}\n")
    elif Manager.info and Manager.interpretations_table:
        if Manager.file_type == FileType.TXT:
            Manager.write("\n")
            txt_interpretations(interps)
        elif Manager.file_type == FileType.TEX:
            Manager.write("\n")
            latex_interpretations(interps)

def demo_write_summary_table():
    if Manager.info and Manager.summary_table:
        if Manager.file_type == FileType.TXT:
            Manager.write("\n")
            Manager.write("################################################################\n")
            Manager.write("#\n")
            Manager.write("#     Summary\n")
            Manager.write("#\n")
            Manager.write("################################################################\n")
            Manager.write("\n")
            txt_summary()
        elif Manager.file_type == FileType.TEX:
            Manager.write("\n")
            Manager.write("\\clearpage\n")
            Manager.write("\n")
            Manager.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
            Manager.write("%\n")
            Manager.write("%     Summary\n")
            Manager.write("%\n")
            Manager.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
            Manager.write("\n")
            Manager.write("\\section*{Summary}\n")
            Manager.write("\\addcontentsline{toc}{section}{Summary}\n")
            Manager.write("\n")
            latex_summary()

def demo_write_lexicon_table():
    if Manager.info and Manager.lexicon_table:
        if Manager.file_type == FileType.TXT:
            Manager.write("\n")
            Manager.write("################################################################\n")
            Manager.write("#\n")
            Manager.write("#     Lexicon\n")
            Manager.write("#\n")
            Manager.write("################################################################\n")
            Manager.write("\n")
            txt_lexicon()
        elif Manager.file_type == FileType.TEX:
            Manager.write("\n")
            Manager.write("\\clearpage\n")
            Manager.write("\n")
            Manager.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
            Manager.write("%\n")
            Manager.write("%     Lexicon\n")
            Manager.write("%\n")
            Manager.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
            Manager.write("\n")
            Manager.write("\\section*{Lexicon}\n")
            Manager.write("\\addcontentsline{toc}{section}{Lexicon}\n")
            Manager.write("\n")
            latex_lexicon()
