def calcCardPos(n):
    page= int(n/9)
    pos = n%9
    col = int(pos%3)
    row= int(pos/3)
    cols = ["left", "center","right"]
    rows=["top","middle","bottom"]
    txt = f"{rows[row]} {cols[col]}"
    return (page,pos,txt)
    


    
while True:
    card = int(input("Card number"))
    page2, pos2, txt2 = calcCardPos(card)
    print("Card", card, "Page", page2, "Pos", pos2, txt2)