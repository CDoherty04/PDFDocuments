from fpdf import FPDF
import pandas as pd

# Creates a pdf with portrait landscape
document = FPDF(orientation="P", unit="mm", format="A4")
document.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

# Read each row in topics.csv
for index, row in df.iterrows():

    # Adds the title page with formatting, text, and a break line
    document.add_page()
    document.set_font(family="Times", size=25, style="B")
    document.set_text_color(10, 10, 50)
    document.cell(w=0, h=12, txt=row["Topic"], align="C", ln=1)
    document.line(10, 25, 200, 25)

    # Create the footer
    document.ln(260)
    document.set_font(family="Times", style="I", size=10)
    document.set_text_color(180, 180, 180)
    document.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)

    # Create a certain number of empty pages as specified by topics.csv
    for i in range(int(row["Pages"])-1):
        document.add_page()

        # Create the footer
        document.ln(272)
        document.set_font(family="Times", style="I", size=10)
        document.set_text_color(180, 180, 180)
        document.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)

document.output("output.pdf")
