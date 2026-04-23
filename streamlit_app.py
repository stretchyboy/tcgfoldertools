import streamlit as st

from cardpos import calcCardPos


st.set_page_config(page_title="TCG Card Position", page_icon="🃏", layout="wide")

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
is_right_page = page % 2 == 1

# Current page is the one containing the highlighted card.
# Opposite page is the blank facing page in the spread.
current_page_number = page
opposite_page_number = page - 1 if is_right_page else page + 1

left_page_number = opposite_page_number if is_right_page else current_page_number
right_page_number = current_page_number if is_right_page else opposite_page_number

st.subheader(f"Page {page} - {label}")

cells = []
for i in range(1, 10):
    card_at_position = ((page - 1) * 9) + i
    if card_at_position == int(card_number):
        cells.append(f'<div class="cell active">{card_at_position}</div>')
    else:
        cells.append(f'<div class="cell">{card_at_position}</div>')

st.markdown(
    """
<style>
.spread {
  display: flex;
  flex-wrap: nowrap;
  justify-content: center;
  align-items: flex-start;
  gap: 10px;
  overflow-x: auto;
  padding: 2px 0;
}
.page {
  width: 248px;
  min-width: 248px;
  margin: 0;
  min-height: 324px;
  border: 2px solid #334155;
  border-radius: 14px;
  padding: 10px;
  background: #ffffff;
}
.page.filled {
  border-color: #0f766e;
  box-shadow: 0 0 0 2px #99f6e4 inset;
}
.page.blank {
  border-style: dashed;
  background: repeating-linear-gradient(
    45deg,
    #f8fafc,
    #f8fafc 10px,
    #f1f5f9 10px,
    #f1f5f9 20px
  );
}
.page-title {
  text-align: center;
  font-size: 0.9rem;
  font-weight: 600;
  color: #0f172a;
  margin-bottom: 8px;
}
.page-content {
  width: 208px;
  min-height: 286px;
  margin: 0 auto;
}
.grid {
  display: grid;
  grid-template-columns: repeat(3, 64px);
  gap: 8px;
  width: 208px;
}
.cell {
  border: 2px solid #1f2937;
  border-radius: 10px;
  aspect-ratio: 5 / 7;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  font-weight: 600;
  background: #f8fafc;
}
.cell.active {
  background: #fde68a;
  border-color: #92400e;
  box-shadow: 0 0 0 2px #f59e0b inset;
}
.blank-fill {
  width: 208px;
  min-height: 286px;
  border-radius: 10px;
  border: 1px dashed #64748b;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #475569;
  font-size: 0.9rem;
  font-weight: 600;
  margin: 0 auto;
}

@media (max-width: 640px) {
  .spread {
    gap: 6px;
  }
  .page {
    width: 166px;
    min-width: 166px;
    min-height: 244px;
    border-radius: 10px;
    padding: 6px;
  }
  .page-title {
    font-size: 0.72rem;
    margin-bottom: 4px;
  }
  .page-content {
    width: 150px;
    min-height: 208px;
  }
  .grid {
    grid-template-columns: repeat(3, 46px);
    gap: 6px;
    width: 150px;
  }
  .cell {
    border-width: 1px;
    border-radius: 7px;
    font-size: 0.8rem;
  }
  .blank-fill {
    width: 150px;
    min-height: 208px;
    font-size: 0.72rem;
  }
}
</style>
""",
    unsafe_allow_html=True,
)


def render_filled_page(page_name, page_cells):
    return f"""
<div class="page filled">
  <div class="page-title">{page_name}</div>
  <div class="page-content">
    <div class="grid">
      {page_cells}
    </div>
  </div>
</div>
"""


def render_blank_page(page_name):
    return f"""
<div class="page blank">
  <div class="page-title">{page_name}</div>
  <div class="page-content">
    <div class="blank-fill">&nbsp;</div>
  </div>
</div>
"""


left_page_html = (
  render_blank_page(f"Left Page ({left_page_number})")
  if is_right_page
  else render_filled_page(f"Left Page ({left_page_number})", "".join(cells))
)
right_page_html = (
  render_filled_page(f"Right Page ({right_page_number})", "".join(cells))
  if is_right_page
  else render_blank_page(f"Right Page ({right_page_number})")
)

st.markdown(
  f"""
<div class="spread">
  {left_page_html}
  {right_page_html}
</div>
""",
  unsafe_allow_html=True,
)

side = "right" if is_right_page else "left"
st.caption(f"Highlighted position {pos}: {label} (page {page}, {side} side of spread)")
