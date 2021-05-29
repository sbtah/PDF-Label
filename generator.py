from fpdf import FPDF
import barcode
from barcode.writer import ImageWriter
import webbrowser



class Generator:
    """
    """

    def __init__(self, filename):
        self.filename = filename

    def generate_barcode(self, ean):
        """
        """
        raw_ean = ean
        my_ean = barcode.get('ean13', raw_ean, writer=ImageWriter())
        my_ean.save(f"Files/{ean}")

    def pdf_ety(self, art1, art2, promotion):#####
        """
        """
        # Generate Page in specified format.
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        # First Article
        # 1st Block
        pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        pdf.set_font(family="DejaVu", size=30)
        pdf.cell(w=0, h=20, txt=art1.name, border=0, align="C", ln=1)

        # 2nd Block
        pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        pdf.set_font(family="DejaVu", size=60)
        pdf.cell(w=0, h=20, txt=art1.cena, border=0, align="C", ln=1)

        # 3rd Block
        pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        pdf.set_font(family="DejaVu", size=20)
        pdf.cell(w=0, h=20, txt=promotion, border=0, align="C", ln=1)

        # Insert a barcode.
        pdf.image(f"Files/{art1.ean}.png", w=200, h=60)

        # !!Insert Margin!!
        pdf.set_font(family="DejaVu", size=20)
        pdf.cell(w=0, h=20, border=0, align="C", ln=1)

        # Second Article
        # 1st Block
        pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        pdf.set_font(family="DejaVu", size=30)
        pdf.cell(w=0, h=20, txt=art2.name, border=0, align="C", ln=1)

        # 2nd Block
        pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        pdf.set_font(family="DejaVu", size=60)
        pdf.cell(w=0, h=20, txt=art2.cena, border=0, align="C", ln=1)

        # 3rd Block
        pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        pdf.set_font(family="DejaVu", size=20)
        pdf.cell(w=0, h=20, txt=promotion, border=0, align="C", ln=1)

        # Insert a barcode.
        pdf.image(f"Files/{art2.ean}.png", w=200, h=60)

        # Generate file.
        pdf.output(f"Files/{self.filename}")
        #webbrowser.open(f"Files/{self.filename}") -this is no longer needed since shareing?
