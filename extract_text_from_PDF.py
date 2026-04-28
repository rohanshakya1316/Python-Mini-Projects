# import PyPDF2

# pdf = open("demo.pdf", "rb")

# reader = PyPDF2.PdfFileReader(pdf)

# page = reader.getPage[0]

# print(page.extract_text())

import PyPDF2

with open("demo.pdf", "rb") as pdf:
    reader = PyPDF2.PdfReader(pdf)
    page = reader.pages[0]
    print(page.extract_text())

