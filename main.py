from fpdf import FPDF
import pandas as pd

# Creates a pdf with portrait landscape
document = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

# Read each row in topics.csv
for index, row in df.iterrows():

    # Create a certain number of new pages as specified by topics.csv
    for i in range(int(row["Pages"])):

        # Adds formatting, text, and a break line to every page
        document.add_page()
        document.set_font(family="Times", size=25, style="B")
        document.set_text_color(10, 10, 50)
        document.cell(w=0, h=12, txt=row["Topic"], align="C", ln=1)
        document.line(10, 25, 200, 25)

document.output("output.pdf")
