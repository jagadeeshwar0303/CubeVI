"""Small constraint parser: user text becomes structured solver options."""

import re


def parse_constraint(text: str) -> dict[str, object]:
    """Parse phrases like 'under 7 moves' into a typed dictionary."""
    # TODO: normalize case/whitespace, extract numbers, recognize supported
    # intents, and return type='unrecognized' for ambiguous text.
    raise NotImplementedError


def constraint_help() -> list[str]:
    """Return examples that can populate a dropdown or help panel."""
    # TODO: keep these examples synchronized with parse_constraint().
    raise NotImplementedError

