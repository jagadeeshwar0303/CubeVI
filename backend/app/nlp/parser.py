import re

def parse_constraint(text):
    normalized = text.lower().strip()
    if not normalized:
        return {"type": "none", "value": None, "raw": text}
    match = re.search(r"(?:under|within|at most|max(?:imum)?)\s+(\d+)", normalized)
    if match:
        return {"type": "max_moves", "value": int(match.group(1)), "raw": text}
    if "shortest" in normalized or "minimum moves" in normalized:
        return {"type": "shortest", "value": True, "raw": text}
    return {"type": "unrecognized", "value": text, "raw": text}

