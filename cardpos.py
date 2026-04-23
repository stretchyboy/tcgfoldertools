def calcCardPos(number):
    if number < 1:
        raise ValueError("Card number must be 1 or greater")

    n = number - 1
    page = (n // 9) + 1
    pos = n % 9
    col = pos % 3
    row = pos // 3
    cols = ["left", "center", "right"]
    rows = ["top", "middle", "bottom"]
    txt = f"{rows[row]} {cols[col]}"
    displaypos = pos + 1
    return (page, displaypos, txt)
    

if __name__ == "__main__":

    while True:
        card = int(input("Card number: "))
        (page2, pos2, txt2) = calcCardPos(card)
        print("Card", card, "Page", page2, "Pos", pos2, txt2)