from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import PyPDF2
import fitz  # PyMuPDF (fitz) library
import os

OUTPUT_FOLDER = "output_files"

def img_to_pdf(input_image_path):
    image = Image.open(input_image_path)
    output_folder_path = os.path.join(os.path.dirname(input_image_path), OUTPUT_FOLDER)
    os.makedirs(output_folder_path, exist_ok=True)
    output_pdf_path = os.path.join(output_folder_path, os.path.splitext(os.path.basename(input_image_path))[0] + ".pdf")

    pdf = canvas.Canvas(output_pdf_path, pagesize=letter)
    pdf.drawImage(input_image_path, 0, 0, width=letter[0], height=letter[1])
    pdf.save()

def pdf_to_img_pypdf2(input_pdf_path):
    output_folder_path = os.path.join(os.path.dirname(input_pdf_path), OUTPUT_FOLDER)
    os.makedirs(output_folder_path, exist_ok=True)
    output_image_path = os.path.join(output_folder_path, os.path.splitext(os.path.basename(input_pdf_path))[0] + ".png")

    with open(input_pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        page = pdf_reader.pages[0]
        xObject = page['/Resources']['/XObject'].get_object()

        for obj in xObject:
            if xObject[obj]['/Subtype'] == '/Image':
                size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
                data = xObject[obj].get_object()
                image = Image.frombytes("RGB", size, data)

                image.save(output_image_path)
                break

def pdf_to_img_pymupdf(input_pdf_path):
    output_folder_path = os.path.join(os.path.dirname(input_pdf_path), OUTPUT_FOLDER)
    os.makedirs(output_folder_path, exist_ok=True)
    output_image_path = os.path.join(output_folder_path, os.path.splitext(os.path.basename(input_pdf_path))[0] + ".png")

    pdf_document = fitz.open(input_pdf_path)
    first_page = pdf_document.load_page(0)
    image_matrix = fitz.Matrix(fitz.Identity)
    image_matrix.prescale(2.0, 2.0)  # Increase scale for better resolution (optional)
    pixmap = first_page.get_pixmap(matrix=image_matrix)

    image = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)
    image.save(output_image_path)

if __name__ == "__main__":
    while True:
        print("1. Convert image to PDF")
        # print("2. Convert PDF to image (PyPDF2)")
        print("2. Convert PDF to image")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            input_image_path = input("Enter the input image file path: ")
            img_to_pdf(input_image_path)
            print("Conversion successful!")

        elif choice == 2:
            input_pdf_path = input("Enter the input PDF file path: ")
            pdf_to_img_pymupdf(input_pdf_path)
            print("Conversion successful!")
            
        elif choice == 3:
            input_pdf_path = input("Enter the input PDF file path: ")
            pdf_to_img_pypdf2(input_pdf_path)
            print("Conversion successful!")


        elif choice == 4:
            break

        else:
            print("Invalid choice. Please try again.")
