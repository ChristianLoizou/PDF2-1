from copy import deepcopy
from pypdf import PdfReader, PdfWriter
from tqdm import tqdm

reader = PdfReader("orig.pdf")

if not len(reader.pages):
    print("PDF has no pages")
    exit()
    
writer = PdfWriter()

for page in tqdm(reader.pages):
    left = deepcopy(page)
    right = deepcopy(page)

    left.mediabox.bottom = page.mediabox.top / 2
    right.mediabox.top /= 2

    writer.add_page(left)
    writer.add_page(right)

with open("output.pdf", 'wb') as outfile:
    writer.write(outfile)