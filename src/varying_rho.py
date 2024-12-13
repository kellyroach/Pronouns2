################################################################
#
#     varying_rho.py
#
################################################################

"""Writes varying_rho output for given example to file."""

from doc import *

def varying_rho_doc(number = "10.1", file: str = "../docs/varying_rho", **kwargs) -> str:
    """Output file containing example sentence with varying rho.

    Args:
        number (optional): str in example_dict. Defaults to "10.1".
        file (str, optional): File name. Defaults to "../docs/varying_rho".
        kwargs: other key-value arguments accepted by Manager.set_state

    Returns:
        str: The full path to the generated file.
    """
    # Set default file_type if not in kwargs
    kwargs['file_type'] = FileType.TEX
    full_path = doc_full_path(kwargs['file_type'], file)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    # Open the file and write content
    with open(full_path, "w", encoding='utf-8') as stream:
        kwargs['stream'] = stream
        with Manager.manager:
            # Update the state of the singleton Manager
            Manager.set_state(**kwargs)
            # Process the example sentence
            ex = example(number)
            sentence = ex[0]
            csn = ex[1]
            Node.set_tree(parse(csn))
            # Write documentation content
            doc_begin()
            for r in range(11):
                rho = 0.1 * r
                varying_rho_demo(number, sentence, rho)
            doc_end()
    return full_path

def varying_rho_demo(number: str, sentence: str, rho: float):
    """Draw chaining diagram using given Spreading Algorithm rho.

    Args:
        number (str): Example sentence identifier in example_dict
        sentence (str): Example sentence == example_dict[number]
        rho (float): In [0.0, 1.0] where 0.0 = not spread out,
            1.0 = completely spread out, and any number in between
            = partially spread out
    """
    with Manager.manager:
        # Update the state of the singleton Manager
        Manager.set_state(info = True, chaining_rho = rho)
        # Write the example number and sentence
        varying_rho_demo_write_number_sentence(number, sentence, rho)
        nnodes = tree_n_nodes(Node.tree())
        chaining(nnodes)
        demo_write_chaining_diagram(nnodes)

def varying_rho_demo_write_number_sentence(number: str, sentence: str, rho: float):
    Manager.write("\n")
    Manager.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
    Manager.write("%\n")
    Manager.write(f"%     Case rho={rho:.1f}\n")
    Manager.write("%\n")
    Manager.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
    Manager.write("\n")
    Manager.write(f"\\section*{{Case \\bm{{${{\\rho={rho:.1f}}}$}}}}\n")
    Manager.write(f"\\addcontentsline{{toc}}{{section}}{{({number}) {sentence}}}\n")
    Manager.write("\n")
    Manager.write("\\bigbreak\n")
    Manager.write("\\begin{enumerate*}\n")
    Manager.write(f"\\item[({number})] {sentence}\n")
    Manager.write("\\end{enumerate*}\n")
    Manager.write("\\bigbreak\n")
