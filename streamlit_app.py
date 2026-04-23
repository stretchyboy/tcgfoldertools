import streamlit as st

from cardpos import calcCardPos


st.set_page_config(page_title="TCG Card Position", page_icon="🃏", layout="centered")

st.title("TCG Card Position Finder")
st.write("Enter a card number to find its page and 3x3 position.")

card_number = st.number_input(
    "Card number",
    min_value=1,
    step=1,
    value=1,
    format="%d",
)

page, pos, label = calcCardPos(int(card_number))

st.subheader(f"Page {page} - {label}")

cells = []
for i in range(1, 10):
    if i == pos:
        cells.append(f'<div class="cell active">{i}</div>')
    else:
        cells.append(f'<div class="cell">{i}</div>')

grid_html = f"""
<style>
.grid {{
  display: grid;
  grid-template-columns: repeat(3, 64px);
  gap: 8px;
  max-width: 208px;
}}
.cell {{
  border: 2px solid #1f2937;
  border-radius: 10px;
  aspect-ratio: 5 / 7;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  font-weight: 600;
  background: #f8fafc;
}}
.cell.active {{
  background: #fde68a;
  border-color: #92400e;
  box-shadow: 0 0 0 2px #f59e0b inset;
}}
</style>
<div class="grid">
  {''.join(cells)}
</div>
"""

st.markdown(grid_html, unsafe_allow_html=True)

st.caption(f"Highlighted position {pos}: {label} (page {page})")
