import sys
import pdfkit
from pdf2docx import Converter

def pdf_to_word(pdf_file, word_file):
    cv = Converter(pdf_file)
    cv.convert(word_file, start=0, end=None)
    cv.close()

def word_to_pdf(word_file, pdf_file):
    pdfkit.from_file(word_file, pdf_file)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Uso: script.py -flag [archivo_entrada] [archivo_salida]")
        sys.exit(1)

    flag = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    if flag == "-pw":
        pdf_to_word(input_file, output_file)
    elif flag == "-wp":
        word_to_pdf(input_file, output_file)
    else:
        print("Banderas válidas: -pw (PDF a Word) o -wp (Word a PDF)")
