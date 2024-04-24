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

    # Educational details
    education = []
    print("\nEnter your educational details:")
    while True:
        degree = input("Degree: ")
        major = input("Major: ")
        university = input("University: ")
        graduation_year = input("Graduation Year: ")

        education.append({
            'degree': degree,
            'major': major,
            'university': university,
            'graduation_year': graduation_year
        })

        more_education = input("Do you want to add more educational details? (yes/no): ").lower()
        if more_education != 'yes':
            break

    # Experience details
    experience = []
    print("\nEnter your experience details:")
    while True:
        title = input("Title: ")
        company = input("Company: ")
        dates = input("Dates (e.g., Jan 2018 - Present): ")
        description = input("Description: ")

        experience.append({
            'title': title,
            'company': company,
            'dates': dates,
            'description': description
        })

        more_experience = input("Do you want to add more experience details? (yes/no): ").lower()
        if more_experience != 'yes':
            break

    # Skills
    skills = input("\nEnter your skills (comma-separated): ").split(',')

    # Projects
    projects = []
    print("\nEnter your projects:")
    while True:
        project_title = input("Project Title: ")
        project_description = input("Project Description: ")

        projects.append({
            'title': project_title,
            'description': project_description
        })

        more_projects = input("Do you want to add more projects? (yes/no): ").lower()
        if more_projects != 'yes':
            break

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

    # Add the image to the PDF
    image_cell = [[Image(img_path, width=img_width, height=img_height)]]
    image_table = Table(image_cell, colWidths=[img_width], rowHeights=[img_height])
    flowables.append(image_table)

    # Add the contact details just opposite to the image without leaving any space
    contact_details = [
        [Paragraph("<b>Name:</b> {}".format(name), normal_style),
         Paragraph("<b>Email:</b> {}".format(email), normal_style),
         Paragraph("<b>Phone:</b> {}".format(phone), normal_style)]
    ]

    contact_table = Table(contact_details, colWidths=[150, 150, 150])
    flowables.append(contact_table)

    # Add the summary to the PDF
    flowables.append(Spacer(1, 12))  # Add space between image and summary
    flowables.append(Paragraph("<b>Summary:</b>", normal_style))
    flowables.append(Paragraph(summary, normal_style))
    flowables.append(Spacer(1, 12))  # Add space between summary and educational details

    # Add educational details
    flowables.append(Paragraph("<b>Educational Details:</b>", normal_style))
    for edu in education:
        flowables.append(Paragraph("Degree: {}".format(edu['degree']), normal_style))
        flowables.append(Paragraph("Major: {}".format(edu['major']), normal_style))
        flowables.append(Paragraph("University: {}".format(edu['university']), normal_style))
        flowables.append(Paragraph("Graduation Year: {}".format(edu['graduation_year']), normal_style))
        flowables.append(Spacer(1, 6))

    # Add experience details
    flowables.append(Paragraph("<b>Experience:</b>", normal_style))
    for exp in experience:
        flowables.append(Paragraph("Title: {}".format(exp['title']), normal_style))
        flowables.append(Paragraph("Company: {}".format(exp['company']), normal_style))
        flowables.append(Paragraph("Dates: {}".format(exp['dates']), normal_style))
        flowables.append(Paragraph("Description: {}".format(exp['description']), normal_style))
        flowables.append(Spacer(1, 6))

    # Add skills
    flowables.append(Paragraph("<b>Skills:</b> {}".format(', '.join(skills)), normal_style))
    flowables.append(Spacer(1, 6))

    # Add projects
    flowables.append(Paragraph("<b>Projects:</b>", normal_style))
    for proj in projects:
        flowables.append(Paragraph("Title: {}".format(proj['title']), normal_style))
        flowables.append(Paragraph("Description: {}".format(proj['description']), normal_style))
        flowables.append(Spacer(1, 6))

    # Build the PDF
    doc.build(flowables)

if __name__ == "__main__":
    output_path = "resume.pdf"  # Output PDF file path (you can change this)
    create_resume(output_path)
    print("Resume generated successfully as 'resume.pdf'.")
