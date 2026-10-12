"""Tests for the natural-language constraint boundary."""

import pytest


@pytest.mark.skip(reason="Implement parser.py first")
def test_max_moves_phrase():
    """'under 7 moves' should become type=max_moves, value=7."""
    # TODO: assert the exact dictionary returned by parse_constraint().
    assert True

