################################################################
#
#    pronouns2.py
#
################################################################

"""Main project Python module to import which imports everything else."""

import argparse
from doc import *
from find_files import *
from varying_rho import *

################################################################
#
#     Module Dependencies
#
# pronouns2
#   find_files
#   varying_rho
#     doc
#       demo
#         examples
#         table_interp
#           view
#             lexicon
#               node_proc
#                 trc
#                   globals
#         table_proc
#           abstract
#             modern
#               tex
#               view
#           chaining
#             modern
#             spread
#               trc
#           latex
#             modern
#           parse_proc
#             lexicon
#           secondary_uty
#             primary_uty
#               trc
#             modern
#             lexicon
#           txt
#             view
#
# NOTE: Except for trc.py, any module which must depend on
# globals.py should indirectly depend on globals.py through
# dependence on some other Python module or trc.py as the
# last resort.  Our strict policy keeps the tree simpler.
################################################################

def main():
    """Main entry point for the pronouns2.py command-line tool.
    
    Supports command line formats:
    python pronouns2.py
    python pronouns2.py "10.1"
    python pronouns2.py --file="MyFile"
    python pronouns2.py "10.1" --file="MyFile"
    python pronouns2.py --help
    
    Additional boolean options from Manager.state can be specified:
    --option_name          (sets option to True)
    --option_name=True/False
    
    Special options:
    --file_type=.txt/.tex (sets output file type)
    --chaining_rho=0.0-1.0 (sets chaining parameter)
    
    Returns:
        None
    """

    # Create parser
    parser = argparse.ArgumentParser(description='Generate analyses for examples')
    # Add positional argument for numbers (optional)
    parser.add_argument('numbers', nargs='?', default=None,
                       help='Example numbers to document (e.g. "10.1")')
    # Add --file argument
    parser.add_argument('--file', default="../docs/Demo",
                       help='Output file path (default: ../docs/Demo)')
    # Add arguments for all Manager.state keys (except 'stream')
    valid_state_keys = set(Manager.manager.state.keys()) - {'stream'}
    for key in valid_state_keys:
        if key == 'chaining_rho':
            parser.add_argument(f'--{key}', type=float,
                              help='Chaining parameter (0.0-1.0)')
        elif key == 'file_type':
            parser.add_argument(f'--{key}', choices=['.txt', '.tex'],
                              help='Output file type')
        else:
            parser.add_argument(f'--{key}', nargs='?', const=True, type=bool,
                              help=f'Set {key} (default: {Manager.manager.state[key]})')
    # Parse arguments
    args = parser.parse_args()
    # Build kwargs dictionary for doc()
    kwargs = {}
    # Handle special cases first
    if args.file_type:
        kwargs['file_type'] = FileType.from_ext(args.file_type)
    if args.chaining_rho is not None:
        if not 0.0 <= args.chaining_rho <= 1.0:
            parser.error("--chaining_rho must be between 0.0 and 1.0")
        kwargs['chaining_rho'] = args.chaining_rho
    # Add all other boolean options from valid_state_keys
    for key in valid_state_keys:
        if key not in {'chaining_rho', 'file_type'}:
            value = getattr(args, key)
            if value is not None:
                kwargs[key] = value
    # Call doc() with parsed arguments
    full_path = doc(numbers=args.numbers, file=args.file, **kwargs)
    print(f"Created: {full_path}")

if __name__ == '__main__':
    main()
