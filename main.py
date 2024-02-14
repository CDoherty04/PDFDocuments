from fpdf import FPDF

document = FPDF(orientation="P", unit="mm", format="A4")

document.add_page()
document.set_font(family="Times", size=15, style="B")
document.cell(w=0, h=12, txt="TITLE", align="C", ln=1)

document.set_font(family="Times", size=12)
document.cell(w=0, h=12, txt="Chill", align="L", ln=1)

document.output("output.pdf")
