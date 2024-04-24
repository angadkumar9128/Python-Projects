from PIL import Image, ImageOps
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import PyPDF2
import os
from reportlab.lib.utils import ImageReader

from pdf import pdf_to_img_pymupdf, pdf_to_img_pypdf2  # Import ImageReader class

OUTPUT_FOLDER = "output_files"
DEFAULT_BACKGROUND_COLOR = (255, 255, 255)  # White background

def img_to_pdf(input_image_path, background_color=DEFAULT_BACKGROUND_COLOR, resize=None, grayscale=False, invert_colors=False):
    original_image = Image.open(input_image_path)

    # Check if the image has an alpha channel
    has_alpha_channel = "A" in original_image.getbands()

    # Change the background color of the image
    if background_color != DEFAULT_BACKGROUND_COLOR:
        new_image = Image.new("RGB", original_image.size, background_color)
        if has_alpha_channel:
            new_image.paste(original_image, mask=original_image.split()[3])  # Preserve alpha channel if present
        else:
            new_image.paste(original_image)
    else:
        new_image = original_image

    # Reduce the image size if requested
    if resize is not None:
        new_image = new_image.resize(resize, Image.ANTIALIAS)

    # Grayscale conversion if requested
    if grayscale:
        new_image = new_image.convert("L")

    # Color inversion if requested
    if invert_colors:
        new_image = ImageOps.invert(new_image)

    output_folder_path = os.path.join(os.path.dirname(input_image_path), OUTPUT_FOLDER)
    os.makedirs(output_folder_path, exist_ok=True)
    output_pdf_path = os.path.join(output_folder_path, os.path.splitext(os.path.basename(input_image_path))[0] + ".pdf")

    pdf = canvas.Canvas(output_pdf_path, pagesize=letter)
    # Convert the PIL image to ImageReader object
    img_reader = ImageReader(new_image)
    pdf.drawImage(img_reader, 0, 0, width=letter[0], height=letter[1])
    pdf.save()

if __name__ == "__main__":
    while True:
        print("1. Convert image to PDF")
        print("2. Convert PDF to image (PyPDF2)")
        print("3. Convert PDF to image (PyMuPDF)")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            input_image_path = input("Enter the input image file path: ")

            bg_color_choice = input("Do you want to change the background color? (y/n): ").lower()
            if bg_color_choice == "y":
                bg_r = int(input("Enter the red value (0-255): "))
                bg_g = int(input("Enter the green value (0-255): "))
                bg_b = int(input("Enter the blue value (0-255): "))
                background_color = (bg_r, bg_g, bg_b)
            else:
                background_color = DEFAULT_BACKGROUND_COLOR

            resize_choice = input("Do you want to resize the image? (y/n): ").lower()
            if resize_choice == "y":
                resize_width = int(input("Enter the new width (in pixels): "))
                resize_height = int(input("Enter the new height (in pixels): "))
                resize = (resize_width, resize_height)
            else:
                resize = None

            grayscale_choice = input("Do you want to convert the image to grayscale? (y/n): ").lower()
            grayscale = True if grayscale_choice == "y" else False

            invert_colors_choice = input("Do you want to invert the colors? (y/n): ").lower()
            invert_colors = True if invert_colors_choice == "y" else False

            img_to_pdf(input_image_path, background_color, resize, grayscale, invert_colors)
            print("Conversion successful!")

        elif choice == 2:
            input_pdf_path = input("Enter the input PDF file path: ")
            pdf_to_img_pymupdf(input_pdf_path)
            print("Conversion successful!")
            # ... (rest of the code remains the same) ...

        elif choice == 3:
            input_pdf_path = input("Enter the input PDF file path: ")
            pdf_to_img_pypdf2(input_pdf_path)
            print("Conversion successful!")
            # ... (rest of the code remains the same) ...

        elif choice == 4:
            break

        else:
            print("Invalid choice. Please try again.")
