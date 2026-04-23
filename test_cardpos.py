from cardpos import calcCardPos


def test_calcCardPos():
    assert calcCardPos(1) == (1, 1, "top left")
    assert calcCardPos(2) == (1, 2, "top center")
    assert calcCardPos(3) == (1, 3, "top right")
    assert calcCardPos(4) == (1, 4, "middle left")
    assert calcCardPos(5) == (1, 5, "middle center")
    assert calcCardPos(6) == (1, 6, "middle right")
    assert calcCardPos(7) == (1, 7, "bottom left")
    assert calcCardPos(8) == (1, 8, "bottom center")
    assert calcCardPos(9) == (1, 9, "bottom right")
    assert calcCardPos(10) == (2, 1, "top left")
    assert calcCardPos(11) == (2, 2, "top center")