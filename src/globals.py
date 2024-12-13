################################################################
#
#    globals.py
#
################################################################

"""Global constants, enums, and data structures for syntax tree processing."""

import sys
from enum import Enum, IntEnum
from typing import Optional

class FeatureIndex(IntEnum):
    """Feature indices for linguistic properties."""
    PNF = 0
    """Pronoun Feature"""
    FPF = 1
    """First Person Feature"""
    SPF = 2
    """Second Person Feature"""
    TPF = 3
    """Third Person Feature"""
    PLF = 4
    """Plural Feature"""
    GNF = 5
    """Gender Feature"""
    ANF = 6
    """Animate Feature"""
    RPF = 7
    """Reflexive Feature"""
    GEN = 8
    """Genitive Feature"""
    def __repr__(self):
        # Dynamically retrieve the class name
        return f"{self.__class__.__name__}.{self.name}"
    def __str__(self):
        # Dynamically retrieve the class name
        return f"{self.__class__.__name__}.{self.name}"

N_FEATURES = len(FeatureIndex)
"""Number of Features"""

HIDE_GEN = False
"""GEN introduced by Chapter 12 in M.S. thesis"""

class NodeId(Enum):
    """Identifies the type of node in the syntax tree."""
    C_NODE = 0
    """Type of Node which represents a C-node."""
    S_NODE = 1
    """Type of Node which represents an S-node."""
    N_NODE = 2
    """Type of Node which represents an N-node."""
    E_NODE = 3
    """Type of Node which represents an E-node."""
    def __repr__(self):
        # Dynamically retrieve the class name
        return f"{self.__class__.__name__}.{self.name}"
    def __str__(self):
        # Dynamically retrieve the class name
        return f"{self.__class__.__name__}.{self.name}"

class Feature(Enum):
    """Represents feature values for linguistic properties."""
    PLUS = 0
    """Node or word has this feature."""
    MINUS = 1
    """Node or word doesn't have this feature."""
    QUESTION = 2
    """Node or word might or might not have this feature."""
    def __repr__(self):
        # Dynamically retrieve the class name
        return f"{self.__class__.__name__}.{self.name}"
    def __str__(self):
        # Dynamically retrieve the class name
        return f"{self.__class__.__name__}.{self.name}"

# Type aliases
Features = list[Feature]
"""Type alias for a list of Feature enums representing linguistic properties."""

class Node:
    """Base node class for syntax tree representation.
    
    Contains fields for tree structure (links), features, and node-specific properties.
    Different node types (C, S, N, E) use different subsets of these fields.
    """
    # Global reference to the current syntax tree
    _tree: Optional['Node'] = None
    def __init__(self):
        """Initializes a new Node with all possible fields set to default values."""
        self.number: int = 0
        self.up_link: Optional['Node'] = None
        self.down_link: Optional['Node'] = None
        self.left_link: Optional['Node'] = None
        self.right_link: Optional['Node'] = None
        self.thread_link: Optional['Node'] = None
        self.np_link: Optional['Node'] = None
        self.chain_link: Optional['Node'] = None
        self.col_link: Optional['Node'] = None
        self.ftr: Features = [Feature.QUESTION] * N_FEATURES
        self.id: NodeId = NodeId.C_NODE
        self.lit: str = ""
        self.end_col_link: Optional['Node'] = None
        self.pred_link: Optional['Node'] = None
        self.succ_link: Optional['Node'] = None
        self.sub: str = ' '
    @property
    def ftr_str(self) -> str:
        result = ['?' if f == Feature.QUESTION else
                  '+' if f == Feature.PLUS else
                  '-' for f in self.ftr]
        if HIDE_GEN:
            result = result[:-1]
        return f"{''.join(result)}"
    @classmethod
    def tree(cls) -> Optional['Node']:
        """Gets the global syntax tree."""
        return cls._tree
    @classmethod
    def set_tree(cls, new_tree: 'Node') -> None:
        """Sets the global syntax tree."""
        cls._tree = new_tree

class FileType(Enum):
    """Controls the output format and detail level."""
    TXT = 0
    """Plain text output"""
    TEX = 1
    """LaTeX formatted output"""
    def __repr__(self):
        # Dynamically retrieve the class name
        return f"{self.__class__.__name__}.{self.name}"
    def __str__(self):
        # Dynamically retrieve the class name
        return f"{self.__class__.__name__}.{self.name}"
    @property
    def file_ext(self):
        """Returns the file extension associated with the file type."""
        type_to_ext = {
            FileType.TXT: ".txt",
            FileType.TEX: ".tex",
        }
        return type_to_ext[self]
    @staticmethod
    def from_ext(ext: str) -> "FileType":
        """Maps a file extension string to its corresponding FileType."""
        ext_to_type = {
            ".txt": FileType.TXT,
            ".tex": FileType.TEX,
        }
        if ext not in ext_to_type:
            raise ValueError(f"Unknown file extension: {ext}")
        return ext_to_type[ext]

class Manager:
    """
    A singleton class for managing output streams and file types.

    The Manager class centralizes state management for output streams 
    and file types used in the application. It maintains a stack of 
    states to allow nested context management with automatic state 
    restoration. The class supports Python "with statement" to manage 
    the active state context and provides class-level methods and 
    properties for accessing and updating the current state.
    """
    manager: Optional['Manager'] = None
    """The singleton instance of the class."""
    def __init__(self):
        self.state = {'stream': sys.stdout,
                      'file_type': FileType.TXT,
                      'info': False,
                      'features_table': True,
                      'abstract_diagram': True,
                      'nodes_after_chaining': True,
                      'nodes_table': True,
                      'chaining_diagram': True,
                      'chaining_rho': 0.5,
                      'chaining_table': True,
                      'interpretations_table': True,
                      'summary_table': True,
                      'lexicon_table': True,
                      'debug': False,
                      'nodes_after_parse': True,
                      'init_table': True,
                      'new_chain': True,
                      'trace': False}
        self.state_stack = []
    def __enter__(self):
        # Push current state onto stack
        self.state_stack.append(self.state.copy())
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Restore previous state, even if exception occurred
        if self.state_stack:
            self.state = self.state_stack.pop()
        return False  # Let exceptions propagate
    @classmethod
    @property
    def state(cls):
        """Class property to return the state of the singleton instance."""
        return cls.manager.state
    @classmethod
    def set_state(cls, **kwargs):
        """Class method to update the state of the singleton instance."""
        if cls.manager is not None:
            # Filter out key-value pairs where value is None
            filtered_kwargs = {key: value for key, value in kwargs.items() if value is not None}
            # Update the state with the filtered dictionary
            cls.manager.state.update(filtered_kwargs)
    @classmethod
    def write(cls, message: str):
        """Writes a message to the currently configured output stream."""
        cls.stream.write(message)
    @classmethod
    @property
    def stream(cls):
        """Class property for 'stream'."""
        return cls.manager.state['stream']
    @classmethod
    @property
    def file_type(cls):
        """Class property for 'file_type'."""
        return cls.manager.state['file_type']
    @classmethod
    @property
    def info(cls):
        """Class property for 'info'."""
        return cls.manager.state['info']
    @classmethod
    @property
    def features_table(cls):
        """Class property for 'features_table'."""
        return cls.manager.state['features_table']
    @classmethod
    @property
    def abstract_diagram(cls):
        """Class property for 'abstract_diagram'."""
        return cls.manager.state['abstract_diagram']
    @classmethod
    @property
    def nodes_table(cls):
        """Class property for 'nodes_table'."""
        return cls.manager.state['nodes_table']
    @classmethod
    @property
    def chaining_diagram(cls):
        """Class property for 'chaining_diagram'."""
        return cls.manager.state['chaining_diagram']
    @classmethod
    @property
    def chaining_rho(cls):
        """Class property for 'chaining_rho'."""
        return cls.manager.state['chaining_rho']
    @classmethod
    @property
    def chaining_table(cls):
        """Class property for 'chaining_table'."""
        return cls.manager.state['chaining_table']
    @classmethod
    @property
    def interpretations_table(cls):
        """Class property for 'interpretations_table'."""
        return cls.manager.state['interpretations_table']
    @classmethod
    @property
    def summary_table(cls):
        """Class property for 'summary_table'."""
        return cls.manager.state['summary_table']
    @classmethod
    @property
    def lexicon_table(cls):
        """Class property for 'lexicon_table'."""
        return cls.manager.state['lexicon_table']
    @classmethod
    @property
    def debug(cls):
        """Class property for 'debug'."""
        return cls.manager.state['debug']
    @classmethod
    @property
    def nodes_after_parse(cls):
        """Class property for 'nodes_after_parse'."""
        return cls.manager.state['nodes_after_parse']
    @classmethod
    @property
    def nodes_after_chaining(cls):
        """Class property for 'nodes_after_chaining'."""
        return cls.manager.state['nodes_after_chaining']
    @classmethod
    @property
    def init_table(cls):
        """Class property for 'init_table'."""
        return cls.manager.state['init_table']
    @classmethod
    @property
    def new_chain(cls):
        """Class property for 'new_chain'."""
        return cls.manager.state['new_chain']
    @classmethod
    @property
    def trace(cls):
        """Class property for 'trace'."""
        return cls.manager.state['trace']
    @classmethod
    @property
    def minimum(cls):
        """Class property for 'minimum'."""
        return (not (cls.manager.state['info']
                     or cls.manager.state['debug']
                     or cls.manager.state['trace']))

# Initialize the singleton inside the class definition
Manager.manager = Manager()

class Summary:
    """Static class to track various info counts in the project.
    
    Contains five integer counters that can be accessed and modified by any module:
    - meaningless: Counter for meaningless items
    - meaningful: Counter for meaningful items 
    - ambiguous: Counter for ambiguous items
    - correct: Counter for correct items
    - total: Total number of items
    """
    meaningless: int = 0
    meaningful: int = 0
    ambiguous: int = 0
    correct: int = 0
    total: int = 0
    @classmethod
    def reset(cls) -> None:
        """Resets all counters to zero."""
        cls.meaningless = 0
        cls.meaningful = 0
        cls.ambiguous = 0
        cls.correct = 0
        cls.total = 0
