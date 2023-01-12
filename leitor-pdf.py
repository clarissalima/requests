import PyPDF2

pdf_file = open('C:\Users\clari\Desktop\LASER\PDFS\Eko.pdf','rb')
PyPDF2.PdfFileReader(pdf_file)

dados_do_pdf = PyPDF2.PdfFileReader(pdf_file)

print(dados_do_pdf.numPages)