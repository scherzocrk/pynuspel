"""Test pynuspell module."""

from pathlib import Path
from pytest import fixture

import pynuspell


@fixture
def dictionary_path():
    """Create path to dictionary."""
    return str(Path(__file__).parent.absolute().joinpath('en-US'))


def test_load_from_path(dictionary_path):
    """Check the type."""
    checker = pynuspell.load_from_path(dictionary_path)
    assert isinstance(checker, pynuspell.Dictionary)


def test_spell_correct(dictionary_path):
    """Check spelling is correct."""
    checker = pynuspell.load_from_path(dictionary_path)
    assert checker.spell('spookier') is True


def test_spell_wrong(dictionary_path):
    """Check spelling is incorrect."""
    checker = pynuspell.load_from_path(dictionary_path)
    assert checker.spell('spookie') is False


def test_suggest(dictionary_path):
    """Get suggestions."""
    checker = pynuspell.load_from_path(dictionary_path)
    assert checker.suggest('spookie') == ['spookier', 'spook']