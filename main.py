from article import Article
from generator import Generator
from file_share import FileSharer
from datetime import date

# Get current day.
today = date.today()

# Get input from a user. Hardcoded values just  for test.
# Article 1.
art_1_name = input("1st article's name: ")  # "NZ SKUWACZ D/LODU TRZON"
art_1_ean =  input("1st article's ean code: ")  # "5906083358784"
art_1_price = input("1st article's unit price: ")  # "29,99"

# Article 2.
art_2_name = input("2nd article's name: ")  # "SZCZOT DRUCIANA 3RZEDOWA"
art_2_ean = input("2nd article's ean code: ")  # "5906083069307
art_2_price = input("1st article's unit price: ")  # "19,99" 

promotion_title = input("Promotion: ").upper()  # "WYPRZEDAŻ" 

# Generate Data for a file.
new_article = Article(name = art_1_name, ean = art_1_ean, cena = art_1_price)
new_article2 = Article(name = art_2_name, ean = art_2_ean, cena = art_2_price)

new_file = Generator(f"Etykieta-{today}.pdf")
new_file.generate_barcode(new_article.ean)

new_file.generate_barcode(new_article2.ean)
new_file.pdf_ety(art1=new_article, art2=new_article2, promotion=promotion_title)

file_sharer = FileSharer(f"Files/Etykieta-{today}.pdf").share()
print(file_sharer)
