#
# AUTOMATICALLY GENERATED FILE, DO NOT EDIT!
#

"""Python bindings for Nuspell - a fast and safe spelling checker C++ library"""
import pynuspell
import typing

__all__ = [
    "Dictionary",
    "load_from_path"
]


class Dictionary():
    def spell(self, arg0: str) -> bool: 
        """
        Checks if a given word is correct
        """
    def suggest(self, arg0: str) -> typing.List[str]: 
        """
        Suggests correct words for a given incorrect word
        """
    pass
def load_from_path(arg0: str) -> Dictionary:
    """
    Create a dictionary from files
    """
