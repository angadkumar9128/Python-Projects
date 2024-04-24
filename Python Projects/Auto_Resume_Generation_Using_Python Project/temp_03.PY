from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from PIL import Image as PILImage
import io

def resize_image(img_path, target_size):
    # Load the image using PIL
    img = PILImage.open(img_path)

    # Resize the image while preserving the aspect ratio
    # img.thumbnail(target_size, PILImage.ANTIALIAS)
    img = img.resize(target_size, PILImage.LANCZOS)


    # Return the resized image
    return img

def create_resume(output_path):
    # Get user resume data
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    summary = input("Enter your summary: ")

    # Get image size from the user
    img_width = int(input("Enter the image width (in pixels): "))
    img_height = int(input("Enter the image height (in pixels): "))
    img_size = (img_width, img_height)

    # Resize user image and attach it to the PDF header
    img_path = input("Enter the path to your image: ")
    img = resize_image(img_path, target_size=img_size)

    # Create a PDF document
    doc = SimpleDocTemplate(output_path, pagesize=letter)
    flowables = []

    # Create a style for the resume content
    normal_style = getSampleStyleSheet()['Normal']

    # Add the image and contact details to the PDF
    image_and_contact = [
        [Image(img_path, width=img_width, height=img_height),
         Paragraph("<b>Name:</b> {}".format(name), normal_style),
         Paragraph("<b>Email:</b> {}".format(email), normal_style),
         Paragraph("<b>Phone:</b> {}".format(phone), normal_style)]
    ]

    image_and_contact_table = Table(image_and_contact, colWidths=[img_width, 150, 150, 150])
    flowables.append(image_and_contact_table)

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
