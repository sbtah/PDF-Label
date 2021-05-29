from article import Article
from generator import Generator

# Get input from a user. Hardcoded values just  for test.
art_1_name = "NZ SKUWACZ D/LODU TRZON"  # input("1st article's name: ")
art_1_ean = "5906083358784"  # input("1st article's ean code: ")
art_1_price = "29,99"  # input("1st article's unit price: ")

art_2_name = "SZCZOT DRUCIANA 3RZEDOWA"  # input("2nd article's name: ")
art_2_ean = "5906083069307"  # input("2nd article's ean code: ")
art_2_price = "19,99"  # input("1st article's unit price: ")

promotion_title = "WYPRZEDAŻ"  # input("Promotion: ").upper()

# Generate Data for a file.
new_article = Article(name = art_1_name, ean = art_1_ean, cena = art_1_price)
new_article2 = Article(name = art_2_name, ean = art_2_ean, cena = art_2_price)
new_file = Generator("ET1.pdf")
new_file.generate_barcode(new_article.ean)
new_file.generate_barcode(new_article2.ean)
new_file.pdf_ety(art1=new_article, art2=new_article2, promotion=promotion_title)