from app.nlp.parser import parse_constraint

def test_max_move_constraint():
    assert parse_constraint("solve it under 7 moves")["value"] == 7

