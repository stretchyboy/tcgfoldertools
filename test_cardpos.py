from cardpos import calcCardPos


def test_calcCardPos():
    assert calcCardPos(1) == (0, 0, "top left")
    assert calcCardPos(2) == (0, 1, "top center")
    assert calcCardPos(3) == (0, 2, "top right")
    assert calcCardPos(4) == (0, 3, "middle left")
    assert calcCardPos(5) == (0, 4, "middle center")
    assert calcCardPos(6) == (0, 5, "middle right")
    assert calcCardPos(7) == (0, 6, "bottom left")
    assert calcCardPos(8) == (0, 7, "bottom center")
    assert calcCardPos(9) == (0, 8, "bottom right")
    assert calcCardPos(10) == (1, 0, "top left")
    assert calcCardPos(11) == (1, 1, "top center")