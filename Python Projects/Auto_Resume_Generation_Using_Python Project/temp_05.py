from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from PIL import Image as PILImage
import io
from reportlab.lib import colors

def resize_image(img_path, target_size):
    # Load the image using PIL
    img = PILImage.open(img_path)

    # Resize the image while preserving the aspect ratio
    # img.thumbnail(target_size, PILImage.ANTIALIAS)
    img = img.resize(target_size, PILImage.LANCZOS)


    # Return the resized image
    return img

def create_resume(output_path):
    # Get image size from the user
    img_width = int(input("Enter the image width (in pixels): "))
    img_height = int(input("Enter the image height (in pixels): "))
    img_size = (img_width, img_height)

    # Resize user image and attach it to the PDF header
    while True:
        try:
            img_path = input("Enter the path to your image: ")
            img = resize_image(img_path, target_size=img_size)
            break
        except FileNotFoundError:
            print("Error: Image file not found. Please provide a valid image path.")

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

    # Educational Details
    educational_details = []
    while True:
        degree = input("Enter your degree: ")
        university = input("Enter the university: ")
        year = input("Enter the year of completion: ")
        educational_details.append([degree, university, year])

        more_education = input("Do you have more educational details? (yes/no): ").lower()
        if more_education != 'yes':
            break

    # Experience
    experience_details = []
    while True:
        company = input("Enter the company name: ")
        position = input("Enter your position: ")
        start_date = input("Enter the start date: ")
        end_date = input("Enter the end date: ")
        experience_details.append([company, position, start_date, end_date])

        more_experience = input("Do you have more experience details? (yes/no): ").lower()
        if more_experience != 'yes':
            break

    # Achievements
    achievements = []
    while True:
        achievement = input("Enter your achievement: ")
        achievements.append(achievement)

        more_achievements = input("Do you have more achievements? (yes/no): ").lower()
        if more_achievements != 'yes':
            break

    # Interests
    interests = []
    while True:
        interest = input("Enter your interest: ")
        interests.append(interest)

        more_interests = input("Do you have more interests? (yes/no): ").lower()
        if more_interests != 'yes':
            break

    # Skills
    skills = []
    while True:
        skill = input("Enter your skill: ")
        skills.append(skill)

        more_skills = input("Do you have more skills? (yes/no): ").lower()
        if more_skills != 'yes':
            break

    # Projects
    projects = []
    while True:
        project = input("Enter your project details: ")
        projects.append(project)

        more_projects = input("Do you have more projects? (yes/no): ").lower()
        if more_projects != 'yes':
            break

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
    table = Table(data, colWidths=[img_width, 400], hAlign="LEFT")
    table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    flowables.append(table)

    # Add the summary to the PDF
    flowables.append(Spacer(1, 12))  # Add space between image+contact and summary
    flowables.append(Paragraph("<b>Summary:</b>", normal_style))
    flowables.append(Paragraph(summary, normal_style))
    flowables.append(Spacer(1, 12))  # Add space between summary and educational details

    # Educational Details
    flowables.append(Paragraph("<b>Educational Details:</b>", normal_style))
    for degree, university, year in educational_details:
        flowables.append(Paragraph(f"- {degree}, {university}, {year}", normal_style))

    # Experience
    flowables.append(Paragraph("<b>Experience:</b>", normal_style))
    for company, position, start_date, end_date in experience_details:
        flowables.append(Paragraph(f"- {company}, {position}, {start_date} to {end_date}", normal_style))

    # Achievement
    flowables.append(Paragraph("<b>Achievement:</b>", normal_style))
    for achievement in achievements:
        flowables.append(Paragraph(f"- {achievement}", normal_style))

    # Interest
    flowables.append(Paragraph("<b>Interest:</b>", normal_style))
    for interest in interests:
        flowables.append(Paragraph(f"- {interest}", normal_style))

    # Skills
    flowables.append(Paragraph("<b>Skills:</b>", normal_style))
    for skill in skills:
        flowables.append(Paragraph(f"- {skill}", normal_style))

    # Projects
    flowables.append(Paragraph("<b>Projects:</b>", normal_style))
    for project in projects:
        flowables.append(Paragraph(f"- {project}", normal_style))

    # Build the PDF
    doc.build(flowables)

if __name__ == "__main__":
    output_path = "resume.pdf"  # Output PDF file path (you can change this)
    create_resume(output_path)
    print("Resume generated successfully as 'resume.pdf'.")
