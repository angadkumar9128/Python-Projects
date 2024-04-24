from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from PIL import Image as PILImage
import io
from reportlab.lib import colors  # Import the colors module

def resize_image(img_path, target_size):
    # Load the image using PIL
    img = PILImage.open(img_path)

    # Resize the image while preserving the aspect ratio
    img = img.resize(target_size, PILImage.LANCZOS)

    # Return the resized image
    return img

def create_resume(output_path):
    # Get user resume data
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    father_name = input("Enter your father's name: ")
    mother_name = input("Enter your mother's name: ")
    alternate_phone = input("Enter your alternate mobile number: ")
    village = input("Enter your village: ")
    district = input("Enter your district: ")
    pincode = input("Enter your pincode: ")
    state = input("Enter your state: ")
    language = input("Enter your language: ")
    summary = input("Enter your summary: ")

    # Get image size from the user
    img_width = int(input("Enter the image width (in pixels): "))
    img_height = int(input("Enter the image height (in pixels): "))
    img_size = (img_width, img_height)

    # Resize user image and attach it to the PDF header
    img_path = input("Enter the path to your image: ")
    try:
        img = resize_image(img_path, target_size=img_size)
    except FileNotFoundError:
        print("Error: Image file not found.")
        return

    # Create a PDF document
    doc = SimpleDocTemplate(output_path, pagesize=letter)
    flowables = []

    # Create a style for the resume content
    normal_style = getSampleStyleSheet()['Normal']

    # Create a table to hold the image and contact details side by side
    data = [
        [Image(img_path, width=img_width, height=img_height),
         Paragraph("<b>Name:</b> {}".format(name), normal_style)],
        ["", Paragraph("<b>Email:</b> {}".format(email), normal_style)],
        ["", Paragraph("<b>Phone:</b> {}".format(phone), normal_style)],
        ["", Paragraph("<b>Father's Name:</b> {}".format(father_name), normal_style)],
        ["", Paragraph("<b>Mother's Name:</b> {}".format(mother_name), normal_style)],
        ["", Paragraph("<b>Alternate Mobile:</b> {}".format(alternate_phone), normal_style)],
        ["", Paragraph("<b>Village:</b> {}".format(village), normal_style)],
        ["", Paragraph("<b>District:</b> {}".format(district), normal_style)],
        ["", Paragraph("<b>Pincode:</b> {}".format(pincode), normal_style)],
        ["", Paragraph("<b>State:</b> {}".format(state), normal_style)],
        ["", Paragraph("<b>Language:</b> {}".format(language), normal_style)]
    ]

    # Create a table with the necessary cell spacing and borders
    table = Table(data, colWidths=[img_width, 420], hAlign="LEFT")
    table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('GRID', (0, 0), (-1, -1), 2,colors.black),
    ]))

    flowables.append(table)

    # Add the summary to the PDF
    flowables.append(Spacer(1, 12))  # Add space between image+contact and summary
    flowables.append(Paragraph("<b>Summary:</b>", normal_style))
    flowables.append(Paragraph(summary, normal_style))
    flowables.append(Spacer(1, 12))  # Add space between summary and educational details

    # ... (add educational details, experience, skills, and projects as before)

    # Build the PDF
    doc.build(flowables)

if __name__ == "__main__":
    output_path = "resume.pdf"  # Output PDF file path (you can change this)
    create_resume(output_path)
    print("Resume generated successfully as 'resume.pdf'.")
