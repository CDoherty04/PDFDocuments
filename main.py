from fpdf import FPDF
import pandas as pd

document = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    for i in range(int(row["Pages"])):
        document.add_page()
        document.set_font(family="Times", size=25, style="B")
        document.set_text_color(10, 10, 50)
        document.cell(w=0, h=12, txt=row["Topic"], align="C", ln=1)
        document.line(10, 25, 200, 25)

document.output("output.pdf")
