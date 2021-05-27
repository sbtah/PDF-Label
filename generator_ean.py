from fpdf import FPDF
from barcode import EAN13
from barcode.writer import ImageWriter
import webbrowser


class Article:
    """
    """
    def __init__(self, name, ean, cena):
        self.name = name
        self.ean = ean
        self.cena = cena



class Generator:
    """
    """
    def __init__(self, filename):
        self.filename = filename


    def generate_barcode(self, ean):
        """
        """
        raw_ean = ean
        my_ean = EAN13(raw_ean, writer=ImageWriter())
        my_ean.save(f"{ean}")
        
        
    def pdf_ety(self):
        """

        """
        # Generate Page in specified format.
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        # First Article
        # 1st Block
        pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        pdf.set_font(family="DejaVu", size=30)
        pdf.cell(w=0, h=20, txt=new_article.name, border=0, align="C", ln=1)

        # 2nd Block
        pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        pdf.set_font(family="DejaVu", size=60)
        pdf.cell(w=0, h=20, txt=new_article.cena, border=0, align="C", ln=1)
        
        # 3rd Block
        pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        pdf.set_font(family="DejaVu", size=20)
        pdf.cell(w=0, h=20, txt=promotion_title, border=0, align="C", ln=1)

        # Insert a barcode.
        pdf.image(f"{new_article.ean}.png", w=200, h=60)


        # !!Insert Margin!!
        pdf.set_font(family="DejaVu", size=20)
        pdf.cell(w=0, h=20, border=0, align="C", ln=1)
        

        # Second Article
        # 1st Block
        pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        pdf.set_font(family="DejaVu", size=30)
        pdf.cell(w=0, h=20, txt=new_article2.name, border=0, align="C", ln=1)

        # 2nd Block
        pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        pdf.set_font(family="DejaVu", size=60)
        pdf.cell(w=0, h=20, txt=new_article2.cena, border=0, align="C", ln=1)
        
        # 3rd Block
        pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        pdf.set_font(family="DejaVu", size=20)
        pdf.cell(w=0, h=20, txt=promotion_title, border=0, align="C", ln=1)

        # Insert a barcode.
        pdf.image(f"{new_article2.ean}.png", w=200, h=60)


        # Generate file.
        pdf.output(self.filename)
        webbrowser.open(self.filename)
        
   


# Get input from a user. Hardcoded values just  for test.
art_1_name = "NZ SKUWACZ D/LODU TRZON" #input("1st articles's name: ")
art_1_ean = "5906083358784" #input("1st articles's ean code: ")
art_1_price = "29,99" #input("1st articles's unit price: ")

art_2_name = "SZCZOT DRUCIANA 3RZEDOWA" #input("2nd articles's name: ")
art_2_ean = "5906083069307" #input("2nd articles's ean code: ")
art_2_price = "19,99" #input("1st articles's unit price: ")

promotion_title = "WYPRZEDAŻ" #input("Promotion: ").upper()

# Generate Data for a file.
new_article = Article(name = art_1_name, ean = art_1_ean, cena = art_1_price)
new_article2 = Article(name = art_2_name, ean = art_2_ean, cena = art_2_price)   
new_file = Generator("ET1.pdf")
new_file.generate_barcode(new_article.ean)
new_file.generate_barcode(new_article2.ean)
new_file.pdf_ety()



